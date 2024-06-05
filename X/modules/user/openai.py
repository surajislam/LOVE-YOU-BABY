from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as kaz
from pyrogram.errors import MessageNotModified
from X.helpers.basic import *
from X.helpers.adminHelpers import DEVS
from config import *
from config import CMD_HANDLER
from config import SUDO_USERS
from X.utils import *
from urllib.parse import quote

import requests
import os
import json
import random

from .help import *

API_ENDPOINTS = [
    "https://api.ajinkya.link/gpt.php?question={question}",
    "https://chatgpt.apinepdev.workers.dev/?question={question}",
    "https://expressional-leaper.000webhostapp.com/chatgpt.php?question={question}"
]

@Client.on_message(
    filters.command(["ai"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def openai(client: Client, message: Message):
    if len(message.command) == 1:
        return await message.reply(f"Ketik <code>.{message.command[0]} [question]</code> Questions for use OpenAI")
    
    question = message.text.split(" ", maxsplit=1)[1]
    
    msg = await message.reply("`Be patient..")

    for endpoint in API_ENDPOINTS:
        url = endpoint.format(question=quote(question))
        
        try:
            response = requests.get(url).json()
            await msg.edit(response["answer"])
            break
        except MessageNotModified:
            pass
        except Exception:
            continue

    else:
        await msg.edit("Sorry, ChatGPT is currently unavailable. Please try again later.")

add_command_help(
    "•─╼⃝𖠁 ᴏᴘᴇɴᴀɪ",
    [
        ["ai", "Tᴏ Aꜱᴋ Sᴏᴍᴇᴛʜɪɴɢ Tᴏ Cʜᴀᴛ Gᴘᴛ"],
    ],
    )
