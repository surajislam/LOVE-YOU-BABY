import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from config import CMD_HANDLER
from config import SUDO_USERS
from X.helpers.basic import edit_or_reply
from X.helpers.PyroHelpers import ReplyCheck
from X.utils.misc import extract_user

from .help import *

flood = {}
profile_photo = "X/modules/cache/pfp.jpg"


@Client.on_message(
    filters.command(["block"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def block_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    X = await edit_or_reply(message, "`Be patient, block again . . .`")
    if not user_id:
        return await message.edit(
            "Provide User ID/Username or reply to user message to unblock."
        )
    if user_id == client.me.id:
        return await X.edit("ANY FOOL CAN BLOCK YOURSELF.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**managed to Block This Dick Kid** {umention}")


@Client.on_message(
    filters.command(["unblock"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def unblock_user_func(client: Client, message: Message):
    user_id = await extract_user(message)
    X = await edit_or_reply(message, "`Be patient and unblock stupid people . . .`")
    if not user_id:
        return await message.edit(
            "Provide User ID/Username or reply to user message to unblock."
        )
    if user_id == client.me.id:
        return await X.edit("If you are stressed, please take medicine immediately.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await message.edit(f"**Successfully Unblocked This Dick Boy ✌** {umention}")


@Client.on_message(
    filters.command(["setname"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def setname(client: Client, message: Message):
    X = await edit_or_reply(message, "`Be patient Change name. . .`")
    if len(message.command) == 1:
        return await X.edit(
            "Provide text to set as your telegram name."
        )
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await X.edit(f"**Successfully changed your Telegram name to** `{name}`")
        except Exception as e:
            await X.edit(f"**ERROR:** `{e}`")
    else:
        return await X.edit(
            "Provide text to set as your telegram name."
        )


@Client.on_message(
    filters.command(["setbio"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def set_bio(client: Client, message: Message):
    X = await edit_or_reply(message, "`Processing . . .`")
    if len(message.command) == 1:
        return await X.edit("Provide text to set as bio.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await X.edit(f"**Successfully Changed your BIO to** `{bio}`")
        except Exception as e:
            await X.edit(f"**ERROR:** `{e}`")
    else:
        return await X.edit("Provide text to set as bio.")


@Client.on_message(
    filters.command(["setpfp"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        await client.download_media(message=replied, file_name=profile_photo)
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.edit("**Your profile photo has been successfully changed.**")
    else:
        await message.edit(
            "`Reply to any photo to set as a profile photo`"
        )
        await sleep(3)
        await message.delete()


@Client.on_message(
    filters.command(["vpfp"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def view_pfp(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id:
        user = await client.get_users(user_id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.edit("Profile photo not found!")
        return
    await client.download_media(user.photo.big_file_id, file_name=profile_photo)
    await client.send_photo(
        message.chat.id, profile_photo, reply_to_message_id=ReplyCheck(message)
    )
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)


add_command_help(
    "•─╼⃝𖠁 ᴘʀᴏғɪʟᴇ",
    [
        ["block", "Tᴏ ʙʟᴏᴄᴋ ᴛᴇʟᴇɢʀᴀᴍ ᴜꜱᴇʀꜱ"],
        ["unblock", "Tᴏ ᴜɴʙʟᴏᴄᴋ ᴛᴇʟᴇɢʀᴀᴍ ᴜꜱᴇʀꜱ"],
        ["setname", "Tᴏ Cʜᴀɴɢᴇ Tᴇʟᴇɢʀᴀᴍ Nᴀᴍᴇ."],
        ["setbio", "Tᴏ Cʜᴀɴɢᴇ Tᴇʟᴇɢʀᴀᴍ Bɪᴏ."],
        [
            "setpfp",
            "Rᴇᴘʟʏ Tᴏ Iᴍᴀɢᴇ Tʏᴘᴇ {cmd}ꜱᴇᴛᴘғᴘ Tᴏ Cʜᴀɴɢᴇ Tᴇʟᴇɢʀᴀᴍ Pʀᴏғɪʟᴇ Pʜᴏᴛᴏ.",
        ],
        ["vpfp", "Tᴏ ꜱᴇᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴜꜱᴇʀ'ꜱ ᴘʀᴏғɪʟᴇ ᴘʜᴏᴛᴏ."],
    ],
  ) 
