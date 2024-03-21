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

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

