import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", "28012365"))
API_HASH = getenv("API_HASH", "40db55020f80e832af2404f81df3e1b4")
BOT_TOKEN = getenv("BOT_TOKEN", "7068876137:AAH-__dcUUYXs2c02mf9yapnWhCaI-J8i4Q")
STRING_SESSION = getenv("STRING_SESSION", "BQGrb00AYPd624hkA8_vPHzvp9xvfwQE7VF6UiI0q6AD45zxqT_rv3s0N3cTXUmNKXfjyK9v_jCZhrprXbY9FXTTKUV26-o5rPZe5LGMgFgtFBpjpv-sd5f7JrESnWIPqs_wZG4PDLgh0iBrWf50qlCcPO0YC-Cah-KMORD4VbgzrGUKMZl8hyuKFjK_GkqEbew2b_PA763CsFEQRbzdL9ce49Z2FRPUnMCobOpkwQNa0hIqhS936rphXAvRs_L9v6P-DzxGTZ4RmdDnaGKxs5vfGExty1XwRgR4jMRi7jPUm2MkRErFmafoarrhT-mnEmtS2HNAub5VGfqUON_WYBzoTdVOJwAAAAHhGt_OAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://heartbeat:Beat7Heart@heartbeat.1h1nbxv.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002584641854"))
OWNER_ID = int(getenv("OWNER_ID", "8071602126"))
OWNER_USERNAME = getenv("OWNER_USERNAME", Ghostt_Batt)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1281282633 8071602126").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://graph.org/file/ffdb1be822436121cf5fd.png")


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", "BQGrb00AYPd624hkA8_vPHzvp9xvfwQE7VF6UiI0q6AD45zxqT_rv3s0N3cTXUmNKXfjyK9v_jCZhrprXbY9FXTTKUV26-o5rPZe5LGMgFgtFBpjpv-sd5f7JrESnWIPqs_wZG4PDLgh0iBrWf50qlCcPO0YC-Cah-KMORD4VbgzrGUKMZl8hyuKFjK_GkqEbew2b_PA763CsFEQRbzdL9ce49Z2FRPUnMCobOpkwQNa0hIqhS936rphXAvRs_L9v6P-DzxGTZ4RmdDnaGKxs5vfGExty1XwRgR4jMRi7jPUm2MkRErFmafoarrhT-mnEmtS2HNAub5VGfqUON_WYBzoTdVOJwAAAAHhGt_OAA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★\n\nʜᴇʏ ɪ'ᴍ 𝐇𝐞𝐚𝐫𝐭𝐁𝐞𝐚𝐭-✗-𝐁𝐨𝐭\n\n☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★\n\n➽─────────────────❥\n\n💕 ᴛᴀɢ ᴍʏ ʟᴏᴠᴇ 🦋\n https://t.me/HeartBeat_Muzic \n\n➽─────────────────❥\n\n😈 ᴏᴛʜᴇʀᴡɪꜱᴇ, ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴍʏ ʙᴏꜱꜱ ᴄᴏᴍᴇꜱ, ᴅᴏɴ'ᴛ ꜱᴘᴀᴍ ᴍᴇ..\nʏᴏᴜ ᴡɪʟʟ ʙᴇ ᴀᴜᴛᴏʙʟᴏᴄᴋ (ᴜᴘᴛᴏ 3 ᴍᴇꜱꜱᴀɢᴇꜱ)\n\n**☆ . * ● ¸ . ✦ .★　° :. ★ * • ○ ° ★**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 3))


# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://graph.org/file/9ee37cccd7bf55c3ec953.png")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("main")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

