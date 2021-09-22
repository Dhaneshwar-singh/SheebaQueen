from SheebaQueen import telethn as tbot
from SheebaQueen.events import register
import os
import asyncio
import os
import time
from datetime import datetime
from SheebaQueen import OWNER_ID
from SheebaQueen import TEMP_DOWNLOAD_DIRECTORY as path
from SheebaQueen import TEMP_DOWNLOAD_DIRECTORY
from datetime import datetime
water = './SheebaQueen/resources/IMG_20210618_123857_189.jpg'
client = tbot

@register(pattern=r"^/send ?(.*)")
async def Prof(event):
    if event.sender_id == OWNER_ID:
        pass
    else:
        return
    thumb = water
    message_id = event.message.id
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./SheebaQueen/modules/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
     message_id = event.message.id
     await event.client.send_file(
             event.chat_id,
             the_plugin_file,
             force_document=True,
             allow_cache=False,
             thumb=thumb,
             reply_to=message_id,
         )
    else:
        await event.reply("No File Found!")


# recoded by @The_Ghost_Hunter | copyright on SheebaQueen


from pyrogram import filters

from SheebaQueen import OWNER_ID
from SheebaQueen import pbot as app


@app.on_message(filters.command("install") & filters.user(OWNER_ID))
async def install_module(_, message):
    if not message.reply_to_message:
        await message.reply_text("Reply To A .py File To Install It.")
        return
    if not message.reply_to_message.document:
        await message.reply_text("Reply To A .py File To Install It.")
        return
    document = message.reply_to_message.document
    if document.mime_type != "text/x-python":
        await message.reply_text("INVALID_MIME_TYPE, Reply To A Correct .py File.")
        return
    m = await message.reply_text("**Installing Module**")
    await message.reply_to_message.download(f"./SheebaQueen/modules/{document.file_name}")
    await m.edit("**Restarting**")
    os.execvp(
        f"python{str(pyver.split(' ')[0])[:3]}",
        [f"python{str(pyver.split(' ')[0])[:3]}", "-m", "SheebaQueen"],
    )
