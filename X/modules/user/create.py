from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply

from .help import *


@Client.on_message(
    filters.command(["create"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def create(client: Client, message: Message):
    if len(message.command) < 3:
        return await edit_or_reply(
            message, f"**Type {cmd}help create if you need help**"
        )
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    Man = await edit_or_reply(message, "`Processing...`")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "gc":  # for supergroup
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**Succeed Make Group Telegram: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )
    elif group_type == "ch":  # for channel
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id["id"])
        await Man.edit(
            f"**Successfully Created Channel Telegram: [{group_name}]({link['invite_link']})**",
            disable_web_page_preview=True,
        )


add_command_help(
    "•─╼⃝𖠁 ᴄʀᴇᴀᴛᴇ",
    [
        ["create ch", "Tᴏ ᴍᴀᴋᴇ ᴄʜᴀɴɴᴇʟ ᴛᴇʟᴇɢʀᴀᴍ Jᴀᴘᴀɴᴇꜱᴇ ᴜꜱᴇʀʙᴏᴛ"],
        ["create gc", "Tᴏ ᴍᴀᴋᴇ ɢʀᴏᴜᴘ ᴛᴇʟᴇɢʀᴀᴍ Jᴀᴘᴀɴᴇꜱᴇ ᴜꜱᴇʀʙᴏᴛ"],
    ],
)
