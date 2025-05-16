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


API_ID = int(getenv("API_ID", "29650844"))
API_HASH = getenv("API_HASH", "6154d581d370cbdadd240292c456d7a2")
BOT_TOKEN = getenv("BOT_TOKEN", "7285188191:AAGNcqe8WaqwnbB399m1CcJfLD4v5W0wJHY")
STRING_SESSION = getenv("STRING_SESSION", "BQHEb5wAjh-VJhJTbGAt_16pIrZF4l6cjP-QxNGnnWSaWCZK7VXM4CeOa-7tvG2zawSFwjJ7j-2RgUSRQFMVNQG1MClEtmKV7gdGGiLliJLyQdAbclUPdpkqSWtyiQHrpekPh98VVCOPR97aryTuNZ1fDfIb5_fq0Ik1HTJNV3pv-YMpL2bcpM6r24rDmu_9v9L1wSkaZAQfXTPFNLZuuOspTwWFf-SWu15jYNn8KGohQOalyPkIDWCozJYarP4gwokvEb4EM55nP7GgeQFmc9YymT0hGoDQfNF91g-AOmCWTSqp2o9rU5EojNImgDc91TbCHS8u7k7TvHixm_JJF2NXzzf6RwAAAAHHZ9BxAA")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://SHASHANK:STRANGER@shashank.uj7lold.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002584641854"))
OWNER_ID = int(getenv("OWNER_ID", "5802254428"))
OWNER_USERNAME = getenv("OWNER_USERNAME", None)
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1281282633 8071602126").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://forestryexplained.co.za/wp-content/uploads/2020/01/Telegram-logo-Featured.jpg")


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", "BQHEb5wAjh-VJhJTbGAt_16pIrZF4l6cjP-QxNGnnWSaWCZK7VXM4CeOa-7tvG2zawSFwjJ7j-2RgUSRQFMVNQG1MClEtmKV7gdGGiLliJLyQdAbclUPdpkqSWtyiQHrpekPh98VVCOPR97aryTuNZ1fDfIb5_fq0Ik1HTJNV3pv-YMpL2bcpM6r24rDmu_9v9L1wSkaZAQfXTPFNLZuuOspTwWFf-SWu15jYNn8KGohQOalyPkIDWCozJYarP4gwokvEb4EM55nP7GgeQFmc9YymT0hGoDQfNF91g-AOmCWTSqp2o9rU5EojNImgDc91TbCHS8u7k7TvHixm_JJF2NXzzf6RwAAAAHHZ9BxAA")
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

