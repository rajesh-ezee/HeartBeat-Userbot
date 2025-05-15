import os
import shutil
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from ... import app, SUDO_USER
from ... import *

@app.on_message(cdz(["restart"]) & (filters.me | filters.user(SUDO_USER)))
async def restart(client: Client, message: Message):
    reply = await message.reply_text("**Restarting...**")
    await message.delete()
    await reply.edit_text("Successfully Restarted \n 𝅗ـﮩ٨ـ𝅽𝅾𓆩𝐇𖽞𖽖֯֟፝͢͡𖽸𖾓𝂬𓏲ࣹ᷼𝄢𝂬𝐁𖽞֟֠֯፝͢͡𖽖𖾓𓆪ﮩ٨ـ𝅽𝅾‐𝅘 Bot...\n\n💞 Wait 1-2 minutes\nLoad plugins...</b>")
    os.system(f"kill -9 {os.getpid()} && python3 -m SHUKLA")
  

__NAME__ = "Rᴇsᴛᴀʀᴛ"
__MENU__ = """
`.restart` **heroku bot restart **
`.upload` **Upload the file to telegram from the given system file path**
"""
