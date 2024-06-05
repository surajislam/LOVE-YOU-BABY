import asyncio

from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(
    filters.command(["ss"], ".") & filters.private & filters.me
)
async def screenshot(bot: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        bot.invoke(
            functions.messages.SendScreenshotNotification(
                peer=await Client.resolve_peer(message.chat.id),
                reply_to_msg_id=0,
                random_id=Client.rnd_id(),
            )
        ),
    )


add_command_help(
    "•─╼⃝𖠁 ꜱᴄʀᴇᴇɴꜱʜᴏᴛ",
    [
        [
            ".ss",
            "Sᴇɴᴅ ᴀ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ ᴀ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ (ɴᴏᴛ ꜱᴇᴄʀᴇᴛ) ᴛᴏ ᴀɴɴᴏʏ ᴏʀ ᴛʀᴏʟʟ ʏᴏᴜʀ ғʀɪᴇɴᴅꜱ.",
        ],
    ],
)
