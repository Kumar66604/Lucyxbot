import asyncio
import importlib
from pyrogram import idle
from Lucyxbot.modules import ALL_MODULES

 

loop = asyncio.get_event_loop()


async def Atomic_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Lucyxbot.modules." + all_module)
    print("»»»» ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


if __name__ == "__main__":
    loop.run_until_complete(Atomic_boot())