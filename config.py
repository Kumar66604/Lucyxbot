from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
PIC = getenv("PIC","").split()
BOT_USERNAME =getenv("BOT_USERNAME","")
MONGO_URI = getenv("MONGO_URI", "mongodb+srv://vikram66604:1234@kicchamoviebot.awkwoux.mongodb.net/?retryWrites=true&w=majority")
#PICS = (environ.get("PICS", "").split()
VIDEO = getenv("VIDEO","https://graph.org/file/8926caeb4948c47b12080.mp4")
SUPPORT_GROUP = getenv("SUPPORT_GROUP","vkmovies02")
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL","vkmovies2")
RAPID_APIKEY = getenv("RAPID_APIKEY", "")
