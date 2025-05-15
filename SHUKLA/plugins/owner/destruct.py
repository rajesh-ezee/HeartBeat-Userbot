import os

from ... import *
from pyrogram import filters


@app.on_message(cdz(["ham","wait","enna","paken","🙄🙄","👀👀","mm","ha"])
    & filters.private & filters.me)
async def self_media(client, message):
    try:
        replied = message.reply_to_message
        if not replied:
            return
        if not (replied.photo or replied.video):
            return
        location = await client.download_media(replied)
        await client.send_document("me", location)
        os.remove(location)
    except Exception as e:
        print("Error: `{e}`")
        return


__NAME__ = "Sᴇʟғ"
__MENU__ = f"""
**🥀 Download And Save Self\n» Destructed Photo Or Video
To Your Saved Message ✨**

`.op` - Use This Command By\nReplying On Self-Destructed
Photo/Video.

**🌿 More Commands:**\n=> ["ham","wait","enna","paken","🙄🙄","👀👀","mm","ha"]
"""
