import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from config import CMD_HANDLER
from config import SUDO_USERS
from X import *
from X.helpers.adminHelpers import DEVS
from X.utils.misc import extract_user_and_reason
from X.helpers.tools import get_arg

from .help import *

ok = []
nyet = [
    "50",
    "350",
    "97",
    "670",
    "24",
    "909",
    "57",
    "89",
    "4652",
    "153",
    "877",
    "890",
]
babi = [
    "2",
    "3",
    "6",
    "7",
    "9"
]


@Client.on_message(
    filters.command(["fgban"], ".") & filters.user(DEVS) & ~filters.me
)
@Client.on_message(
    filters.command(["fgban"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def fgban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`Gbaning...`")
    else:
        ex = await message.edit("`GBANNING!`")
    if not user_id:
        return await ex.edit("Reply to user messages or provide username/user_id")
    if user_id == client.me.id:
        return await ex.edit("**Do you want to ban yourself? Stupid!**")
    if user_id in DEVS:
        return await ex.edit("**Devs You can't ban it, you bastard, only God can🗿**")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Reply to user messages or provide username/user_id`")        
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#GBanned**"
        f"\n\n**Name:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    msg += f"\n**Success Of:** `{done}` **Chat**"
    await asyncio.sleep(5)
    await ex.edit(msg)

@Client.on_message(
    filters.command("fgmute", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(
    filters.command(["fgmute"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def fgmute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`GMuting...`")
    else:
        ex = await message.edit("`Gmuting...`")
    if not user_id:
        return await ex.edit("Reply to user messages or provide username/user_id")
    if user_id == client.me.id:
        return await ex.edit("**Do you want to mute yourself? Stupid!**")
    if user_id in DEVS:
        return await ex.edit("**Devs You can't ban it, you bastard, only God can🗿**")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Reply to user messages or provide username/user_id`")
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#GMuted**"
        f"\n\n**Namae** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    msg += f"\n**Sukses Of:** `{done}` **Chat**"
    await asyncio.sleep(5)
    await ex.edit(msg)

@Client.on_message(
    filters.command("fgkick", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(
    filters.command(["fgkick"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def fgkick(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    if message.from_user.id != client.me.id:
        ex = await message.reply_text("`GKick...`")
    else:
        ex = await message.edit("`Gkicking...!`")
    if not user_id:
        return await ex.edit("Reply to user messages or provide username/user_id")
    if user_id == client.me.id:
        return await ex.edit("**Do you want to kick yourself? Stupid!**")
    if user_id in DEVS:
        return await ex.edit("**Devs You can't kick it, you bastard, only God can🗿**")
    if user_id:
        try:
            user = await client.get_users(user_id)
        except Exception:
            return await ex.edit("`Reply to user messages or provide username/user_id`")
    ok.append(user.id)
    done = random.choice(nyet)
    msg = (
        r"**#GKicked**"
        f"\n\n**Name:** [{user.first_name}](tg://user?id={user.id})"
        f"\n**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    msg += f"\n**Success of:** `{done}` **Chat**"
    await asyncio.sleep(5)
    await ex.edit(msg)


@Client.on_message(
    filters.command("fgcast", ["."]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(
    filters.command(["fgcast"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def fgcast(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = random.choice(nyet)
    fail = random.choice(babi)
    await asyncio.sleep(5)
    await tex.edit_text(
        f"**Successfully Sent Message To** `{done}` **Groups chat, Failed to Send Message To** `{fail}` **Groups**"
    )

add_command_help(
    "•─╼⃝𖠁 Fᴀᴋᴇ",
    [
        [f"gban <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Fᴀᴋᴇ Gʟᴏʙᴀʟ Bᴀɴɴɪɴɢ."],
        [f"gmute <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Fᴀᴋᴇ Gʟᴏʙᴀʟ Mᴜᴛᴇ."],
        [f"gkick <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Fᴀᴋᴇ Gʟᴏʙᴀʟ Kɪᴄᴋ."],
        [f"gcast <ʀᴇᴘʟʏ/ᴜꜱᴇʀɴᴀᴍᴇ/ᴜꜱᴇʀɪᴅ>", "Fᴀᴋᴇ Gʟᴏʙᴀʟ ʙʀᴏᴀᴅᴄᴀꜱᴛ."],
    ],
  )
