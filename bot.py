import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv  # dotenv import karein

# Load .env file
load_dotenv()

# Bot Config (Environment Variables)
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
IMGBB_API_KEY = os.getenv("IMGBB_API_KEY")

app = Client("catbox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Start Command
@app.on_message(filters.command("start"))
def start(client, message: Message):
    message.reply_text(
        "Ｗᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ GOD LINK BOX! 🐾\n\n"
        "ꜱᴇɴᴅ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ ᴀ ᴜʀʟ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ IMGBB, ᴀɴᴅ ɪ'ʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ʟɪɴᴋ ʙᴀᴄᴋ!💖"
    )

# Image Upload Handler
@app.on_message(filters.photo)
def upload_image(client, message: Message):
    file_path = client.download_media(message.photo.file_id)

    with open(file_path, "rb") as image_file:
        files = {"image": image_file}
        data = {"key": IMGBB_API_KEY}
        response = requests.post("https://api.imgbb.com/1/upload", files=files, data=data)

    os.remove(file_path)

    if response.status_code == 200:
        imgbb_link = response.json()["data"]["url"]
        message.reply_text(f"🖼️ Image uploaded! Here is your link: {imgbb_link}")
    else:
        message.reply_text("❌ Failed to upload image. Try again later.")

app.run()