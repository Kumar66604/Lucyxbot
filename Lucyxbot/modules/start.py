from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Lucyxbot import app

@app.on_message(filters.command("st"))
async def start(_, message):
    await message.reply_text("Hello! I am your bot. How can I help you?")
