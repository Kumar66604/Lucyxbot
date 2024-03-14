import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.types import InputMediaVideo
from Lucyxbot import app
from config import PIC, BOT_USERNAME, VIDEO, SUPPORT_GROUP, UPDATE_CHANNEL


@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [[
            InlineKeyboardButton('🥀 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘs 🥀', url=f'https://t.me/{BOT_USERNAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🥀 Sᴜᴘᴘᴏʀᴛ 🥀', url=f'https://t.me/{SUPPORT_GROUP}'),
            InlineKeyboardButton('🥀 Uᴘᴅᴀᴛᴇs 🥀', url=f'https://t.me/{UPDATE_CHANNEL}')
    ],[
            InlineKeyboardButton('✨ Cᴏᴍᴍᴀɴᴅs ✨', callback_data="commands")
    ],[
            InlineKeyboardButton('✨ Sᴏᴜʀᴄᴇ ✨', callback_data="source")
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await msg.reply_photo(
        photo=random.choice(PIC),
        caption="""𝙷𝙴𝚈 𝚃𝙷𝙴𝚁𝙴! 🥀 {},\n👋 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 <a href=f"https://t.me/{BOT_USERNAME}?start=your_start_parameter">➳❥ɪᴹ᭄𝑳𝒖𝒄𝒚 𝒙 𝒃𝒐𝒕 🫧</a>,\n\n<b>𝙸 𝚊𝚖 𝚑𝚎𝚛𝚎 𝚝𝚘 𝚊𝚜𝚜𝚒𝚜𝚝 𝚢𝚘𝚞 𝚠𝚒𝚝𝚑 𝚟𝚊𝚛𝚒𝚘𝚞𝚜 𝚝𝚊𝚜𝚔𝚜. 𝙵𝚎𝚎𝚕 𝚏𝚛𝚎𝚎 𝚝𝚘 𝚎𝚡𝚙𝚕𝚘𝚛𝚎 𝚝𝚑𝚎 𝚊𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊𝚗𝚍 𝚏𝚎𝚊𝚝𝚞𝚛𝚎𝚜.</b>\n\n""".format(msg.from_user.mention),
        reply_markup=reply_markup
    )

@app.on_message(filters.command(["help"]) & filters.group)
async def help_command(client, message):
    start_button_link = f"https://t.me/{BOT_USERNAME}?start=your_start_parameter"
    caption = "⟳ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴍʏ ʜᴇʟᴘ ᴍᴇɴᴜ ɪɴ ʏᴏᴜʀ ᴘᴍ "

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("⟳ ʜᴇʟᴘ ⟳", url=start_button_link)],
        ]
    )

    await message.reply_text(caption, reply_markup=keyboard)
@app.on_callback_query()
async def callback_query_handler(client, query):
    if query.data == 'home':
        ghelp_text1 = (
             """𝙷𝙴𝚈 𝚃𝙷𝙴𝚁𝙴! 🥀 ,\n👋 𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 <a href=f"https://t.me/{BOT_USERNAME}?start=your_start_parameter">➳❥ɪᴹ᭄𝑳𝒖𝒄𝒚 𝒙 𝒃𝒐𝒕 🫧</a>,\n\n<b>𝙸 𝚊𝚖 𝚑𝚎𝚛𝚎 𝚝𝚘 𝚊𝚜𝚜𝚒𝚜𝚝 𝚢𝚘𝚞 𝚠𝚒𝚝𝚑 𝚟𝚊𝚛𝚒𝚘𝚞𝚜 𝚝𝚊𝚜𝚔𝚜. 𝙵𝚎𝚎𝚕 𝚏𝚛𝚎𝚎 𝚝𝚘 𝚎𝚡𝚙𝚕𝚘𝚛𝚎 𝚝𝚑𝚎 𝚊𝚟𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊𝚗𝚍 𝚏𝚎𝚊𝚝𝚞𝚛𝚎𝚜.</b>\n\n"""
        )
        buttons1 = [[
            InlineKeyboardButton('🥀 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘs 🥀', url=f'https://t.me/{BOT_USERNAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🥀 Sᴜᴘᴘᴏʀᴛ 🥀', url=f'https://t.me/vkmovies02'),
            InlineKeyboardButton('🥀 Uᴘᴅᴀᴛᴇs 🥀', url=f'https://t.me/vkmovies2')
    ],[
            InlineKeyboardButton('✨ Cᴏᴍᴍᴀɴᴅs ✨', callback_data="commands")
    ],[
            InlineKeyboardButton('✨ Sᴏᴜʀᴄᴇ ✨', callback_data="source")
    ]]
        reply_markup1 = InlineKeyboardMarkup(buttons1)
        await query.message.edit_text(ghelp_text1, reply_markup=reply_markup1)
    elif query.data == 'commands':
        ghelp_text = (
             " <b>Pᴏᴡᴇʀs Oғ </b><a href='https://t.me/lucy666xbot'>➳❥ɪᴹ᭄𝑳𝒖𝒄𝒚 𝒙 𝒃𝒐𝒕 🫧</a> "
        )
        buttons = [[
            InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home"),
            InlineKeyboardButton("⟳ ᴄʟᴏsᴇ ⟳", callback_data="close")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(ghelp_text, reply_markup=reply_markup)
    elif query.data == "source":
        await query.edit_message_media(
        media=InputMediaVideo(VIDEO, has_spoiler=True),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="⟳ ʙᴀᴄᴋ ⟳", callback_data="close")]
            ]
        ),
        )
    elif query.data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
