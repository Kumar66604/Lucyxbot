import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from Lucyxbot import app
from config import PIC, BOT_USERNAME

@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [[
            InlineKeyboardButton('🥀 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘs 🥀', url=f'https://t.me/{BOT_USERNAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🥀 Sᴜᴘᴘᴏʀᴛ 🥀', url='https://t.me/vkmovies02'),
            InlineKeyboardButton('🥀 Uᴘᴅᴀᴛᴇs 🥀', url='https://t.me/vkmovies2')
    ],[
            InlineKeyboardButton('✨ Cᴏᴍᴍᴀɴᴅs ✨', callback_data="commands")
    ],[
            InlineKeyboardButton('✨ Sᴏᴜʀᴄᴇ ✨', url=f'https://t.me/{BOT_USERNAME}?start=true')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_photo(
        photo=random.choice(PIC),
        caption="""𝙷𝙴𝚈 𝚃𝙷𝙴𝚁𝙴! 🥀 {},\n👋 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 <a href='https://t.me/lucy666xbot'>➳❥ɪᴹ᭄𝑳𝒖𝒄𝒚 𝒙 𝒃𝒐𝒕 🫧</a>,\n\n<b>𝙸 𝚊𝚖 𝚑𝚎𝚛𝚎 𝚝𝚘 𝚊𝚜𝚜𝚒𝚜𝚝 𝚢𝚘𝚞 𝚠𝚒𝚝𝚑 𝚟𝚊𝚛𝚒𝚘𝚞𝚜 𝚝𝚊𝚜𝚔𝚜. 𝙵𝚎𝚎𝚕 𝚏𝚛𝚎𝚎 𝚝𝚘 𝚎𝚡𝚙𝚕𝚘𝚛𝚎 𝚝𝚑𝚎 𝚊𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊𝚗𝚍 𝚏𝚎𝚊𝚝𝚞𝚛𝚎𝚜.</b>\n\n""".format(msg.from_user.mention),
        reply_markup=reply_markup
    )

@app.on_callback_query()
def callback_query_handler(client, query):
    if query.data == 'commands':
        ghelp_text = (
             " <b>Pᴏᴡᴇʀs Oғ </b><a href='https://t.me/lucy666xbot'>➳❥ɪᴹ᭄𝑳𝒖𝒄𝒚 𝒙 𝒃𝒐𝒕 🫧</a> "
        )
        buttons = [
            [
                InlineKeyboardButton("Close 🔐", callback_data="close")
            ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        query.message.edit_text(ghelp_text, reply_markup=reply_markup)
        

@app.on_callback_query(filters.regex("close"))
async def closeh(_, query):
  chat_id = query.chat.id
  await query.message.delete()

