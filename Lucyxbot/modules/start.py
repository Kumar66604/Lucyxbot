import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Lucyxbot import app
from config import PIC, BOT_USERNAME

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [[
            InlineKeyboardButton('➕ Add Me To Your Groups ➕', url=f'https://t.me/{BOT_USERNAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🔍 support', url='https://t.me/vkmovies02'),
            InlineKeyboardButton('🤖 Updates', url='https://t.me/vkmovies2')
    ],[
            InlineKeyboardButton('⚡ COMMANDS ⚡', url=f'https://t.me/{BOT_USERNAME}?start=true')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_photo(
        photo=random.choice(PIC),
        caption="""𝙷𝙴𝙻𝙾 {},\n👋 Welcome to <a href='https://t.me/lucy666xbot'>➳❥ɪᴹ᭄𝑳𝒖𝒄𝒚 𝒙 𝒃𝒐𝒕 🫧</a>,\n\n<b>I am here to assist you with various tasks.Feel free to explore the available commands and features.</b>\n\n""".format(msg.from_user.mention),
        reply_markup=reply_markup
    )


