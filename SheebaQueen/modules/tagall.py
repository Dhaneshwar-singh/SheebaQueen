import asyncio

from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins

from SheebaQueen import telethn
from SheebaQueen.events import register as Sheeba



@Sheeba(pattern="^/tagall ?(.*)")
async def _(event):
    if event.fwd_from:
        return
    mentions = f"Hi Friends I'm Sheeba_Queen I Call To All Of You"
    chat = await event.get_input_chat()
    async for x in telethn.iter_participants(chat, 100):
        mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()

__mod_name__ = "Tag All"
__help__ = """
  ➢ `/tagall` : Tag everyone in a chat.
  ➢ `/tagall` : Mention All Members
Exp:- /all <Text> or <reply>
Note:- This `/tagall` Command can mention members upto 10,000 in groups and can mention members upto 200 in channels !
"""
