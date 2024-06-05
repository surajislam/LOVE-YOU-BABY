import asyncio

import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply
from .help import *


@Client.on_message(
    filters.command(["neko", "nekobin", "bin", "paste"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def paste(bot: Client, message: Message):
    text = message.reply_to_message.text
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    "https://nekobin.com/api/documents", json={"content": text}, timeout=3
            ) as response:
                key = (await response.json())["result"]["key"]
    except Exception:
        await message.edit_text("`Pasting failed`")
        await asyncio.sleep(2)
        await message.delete()
        return
    else:
        url = f"https://nekobin.com/{key}"
        reply_text = f"Nekofied to **Nekobin** : {url}"
        delete = (
            True
            if len(message.command) > 1
               and message.command[1] in ["d", "del"]
               and message.reply_to_message.from_user.is_self
            else False
        )
        if delete:
            await asyncio.gather(
                bot.send_message(
                    message.chat.id, reply_text, disable_web_page_preview=True
                ),
                message.reply_to_message.delete(),
                message.delete(),
            )
        else:
            await message.edit_text(
                reply_text,
                disable_web_page_preview=True,
            )


add_command_help(
    "•─╼⃝𖠁 ᴘᴀꜱᴛᴇ",
    [
        [
            ".paste `or` .bin `or` .neko `or` .nekobin",
            "Cʀᴇᴀᴛᴇ ᴀ Nᴇᴋᴏʙɪɴ ᴘᴀꜱᴛᴇ ᴜꜱɪɴɢ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇꜱꜱᴀɢᴇ.",
        ],
    ],
      )
