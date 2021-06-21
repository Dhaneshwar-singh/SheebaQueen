import asyncio

from SheebaQueen import telethn as sheeba


@sheeba(pattern="pprank")
async def pprank(ult):
    if not ult.text[0].isalpha() and ult.text[0] not in ("/", "#", "@", "!"):
        msg = await eor(ult, "**PROMOTING USER..**")
        await asyncio.sleep(1)
        await msg.edit("**PROMOTING USER...**")
        await asyncio.sleep(1)
        await msg.edit("**GIVING RIGHTS**")
        await asyncio.sleep(1)
        await msg.edit("**PROMOTED USER SUCCESSFULLY**")
