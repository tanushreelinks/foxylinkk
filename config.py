#(©)foxylinkk




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7686713086:AAGfTAxfaeSNN015DO53KXYy63zDX_0sL2k")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25928407"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d0824f557b06f6c87b0b0ce1e7c2f1e4")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002285688282"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7299439165"))

#Port
PORT = os.environ.get("PORT", "8087")

#Database 
DB_URI = "mongodb+srv://Subhashreetoken:Lord4gent@subhashreetoken.hepjw.mongodb.net/?retryWrites=true&w=majority&appName=Subhashreetoken"
DB_NAME = os.environ.get("DATABASE_NAME", "nxx")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "54335b798ddf24239b147c499daeb1f629951839")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 21600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://youtu.be/1A3C0xnLDfc?si=6dWwf7YlgmbKztZ1")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "https://t.me/+OybAqfXxT5E1ZjA1"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel https://t.me/+OybAqfXxT5E1ZjA1 and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7362655192").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group https://t.me/+OybAqfXxT5E1ZjA1 to use me\n\nKindly Please join Channel<https://t.me/+OybAqfXxT5E1ZjA1>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We LeakHubd or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly @foxylinkk!"

ADMINS.append(OWNER_ID)
ADMINS.append(7362655192)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
