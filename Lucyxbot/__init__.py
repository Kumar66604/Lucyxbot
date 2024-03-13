import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "Lucyxbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

print("🐾 I'm Alive Now 😀 🐾")
app.run()
