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
]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
        photo=random.choice(PIC),
        caption="""𝙷𝙴𝙻𝙾 {},\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>, 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 😍""",
        reply_markup=reply_markup
    )


