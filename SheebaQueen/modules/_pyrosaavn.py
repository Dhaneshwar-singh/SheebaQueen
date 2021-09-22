# recoded by @The_Ghost_Hunter on Telegram. 

import requests
import wget
from pyrogram import filters

from SheebaQueen import pbot as app 
from SheebaQueen.pyrogramee.dark import get_arg


@app.on_message(filters.command("saavn") & ~filters.edited)
async def jssong(_, message):
    global is_downloading
    if len(message.command) < 2:
        return await message.reply_text(
            "/saavn requires an argument."
        )
    if is_downloading:
        return await message.reply_text(
            "Another download is in progress, try again after sometime."
        )
    is_downloading = True
    text = message.text.split(None, 1)[1]
    m = await message.reply_text("Searching...")
    try:
        songs = await arq.saavn(text)
        if not songs.ok:
            await m.edit(songs.result)
            is_downloading = False
            return
        sname = songs.result[0].song
        slink = songs.result[0].media_url
        ssingers = songs.result[0].singers
        await m.edit("Downloading")
        song = await download_song(slink)
        await m.edit("Uploading")
        await message.reply_audio(
            audio=song,
            title=sname,
            performer=ssingers,
        )
        os.remove(song)
        await m.delete()
    except Exception as e:
        is_downloading = False
        return await m.edit(str(e))
    is_downloading = False
