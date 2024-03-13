from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
PIC = getenv("PIC","").split()
BOT_USERNAME =getenv("BOT_USERNAME","")
#PICS = (environ.get("PICS", "").split()
