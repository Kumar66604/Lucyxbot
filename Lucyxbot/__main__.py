from pyrogram import Client, filters
from config import *

app = Client(
    "Lucyxbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("🐾 I'm Alive Now 😀 🐾")
app.run()
