



import codecs
import pickle
from typing import Dict, List, Union

from SheebaQueen import db



chatbotdb = db.chatbotdb

async def check_chatbot():
    return (
        await chatbotdb.find_one({"chatbot": "chatbot"}) or {"bot": [], "userbot": []}
    )

async def add_chatbot(chat_id: int, is_userbot: bool = False):
    list_id = await check_chatbot()
    if is_userbot:
        list_id["userbot"].append(chat_id)
    else:
        list_id["bot"].append(chat_id)
    await chatbotdb.update_one({"chatbot": "chatbot"}, {"$set": list_id}, upsert=True)


async def rm_chatbot(chat_id: int, is_userbot: bool = False):
    list_id = await check_chatbot()
    if is_userbot:
        list_id["userbot"].remove(chat_id)
    else:
        list_id["bot"].remove(chat_id)
    await chatbotdb.update_one({"chatbot": "chatbot"}, {"$set": list_id}, upsert=True)