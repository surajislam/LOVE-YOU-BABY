import asyncio
from random import choice
from pyrogram.types import Message
from pyrogram import filters, Client
from config import OWNER_ID
from config import SUDO_USERS
from config import CMD_HANDLER as cmd
from XDB.data import GROUP, PORM
from .help import *

@Client.on_message(
    filters.command(["pspam"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def pspam(client: Client, message: Message):
    cid = message.chat.id
    if int(cid) in GROUP:
        await message.reply_text("𝐬𝐫𝐲, 𝐭𝐡𝐢𝐬 𝐠𝐫𝐩 𝐢𝐬 𝐩𝐫𝐨𝐭𝐞𝐜𝐭𝐞𝐝 𝐛𝐲 𝐬𝐨𝐦𝐞 𝐯𝐢𝐬𝐮𝐚𝐥 𝐩𝐨𝐰𝐞𝐫𝐬 🛡️")
        return

    altp = message.text.split(" ", 2)
    if len(altp) > 1:
        quantity = int(altp[1])
        for _ in range(quantity):
            porm = choice(PORM)
            await client.send_video(cid, porm)
            await asyncio.sleep(0.3)
    else:
        await message.reply_text(f".𝐩𝐬𝐩𝐚𝐦 13")


add_command_help(
    "•─╼⃝𖠁 ᴘᴏʀɴ",
    [
        ["pspam", "Tᴏ ꜱᴇɴᴅ ᴘᴏʀɴ ᴠɪᴅᴇᴏ."],
    ],
  )
