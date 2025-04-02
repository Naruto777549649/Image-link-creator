import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# Bot Config
API_ID = "25698862"
API_HASH = "7d7739b44f5f8c825d48cc6787889dbc"
BOT_TOKEN = "7687739757:AAHJZ4Ic3MeYq28GItW9mQSNWgigYBIUihw"
IMGBB_API_KEY = "fadbcc22a78ae0a3c458d30c9aa52713"

app = Client("catbox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=>

# Start Command
@app.on_message(filters.command("start"))
def start(client, message: Message):
    message.reply_text(
        "Ｗᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ GOD LINK BOX! 🐾\n\n"
        "ꜱᴇɴᴅ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ ᴀ ᴜʀʟ ᴛᴏ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ IMGBB, ᴀɴᴅ ɪ'ʟʟ ɢɪᴠᴇ ʏᴏ>
    )

# Image Upload Handler
@app.on_message(filters.photo)
def upload_image(client, message: Message):
    file_path = client.download_media(message.photo.file_id)

    with open(file_path, "rb") as image_file:
        files = {"image": image_file}
        data = {"key": IMGBB_API_KEY}
        response = requests.post("https://api.imgbb.com/1/upload", file>

    os.remove(file_path)

    if response.status_code == 200:
        imgbb_link = response.json()["data"]["url"]
        message.reply_text(f"🖼️ Image uploaded! Here is your link: {imgb>
    else:
        message.reply_text("❌ Failed to upload image. Try again later.>

app.run()
