import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message

from config import SUDO_USERS
from X.helpers.PyroHelpers import GetChatID, ReplyCheck
from .help import * 

@Client.on_message(
    filters.command(["genshin"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_genshin(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/genshin"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
              )

@Client.on_message(
    filters.command(["swimsuit"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_swimsuit(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/swimsuit"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(
    filters.command(["schoolswimsuit"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_schoolswimsuit(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/schoolswimsuit"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(
    filters.command(["white"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_white(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/white"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(
    filters.command(["barefoot"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_barefoot(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/barefoot"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(
    filters.command(["touhou"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_bully(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/touhou"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )
@Client.on_message(
    filters.command(["gamecg"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_bully(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/gamecg"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(
    filters.command(["hololive"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_bully(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/hololive"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(
    filters.command(["uncensored"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_bully(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/uncensored"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )

@Client.on_message(
    filters.command(["sunglasses"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def give_bully(bot: Client, message: Message):
    URL = "https://fantox-apis.vercel.app/sunglasses"
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.edit("`no anime for you :c")
            result = await request.json()
            url = result.get("url", None)
            
            if message.reply_to_message and message.reply_to_message.from_user:
                replied_user = message.reply_to_message.from_user
                user_first_name = replied_user.first_name
                user_id = replied_user.id
                user_link = f"[{user_first_name}](tg://user?id={user_id})"
                caption = f"ғᴏʀ ʏᴏᴜ {user_link}"
            else:
                return await message.edit("ᴘʟᴇᴀꜱᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ʀᴇᴀᴄᴛ ᴛᴏ ꜱᴏᴍᴇᴏɴᴇ.")
            
            await asyncio.gather(
                message.delete(),
                bot.send_video(
                    GetChatID(message), url, 
                    reply_to_message_id=ReplyCheck(message),
                    caption=caption
                ),
            )


add_command_help(
    "•─╼⃝𖠁 ᴀɴɪᴍᴇ",
    [
       ["genshin", "Gɪᴠᴇ genshin."],
       ["swimsuit", "Gɪᴠᴇ swimsuit ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["schoolswimsuit", "Gɪᴠᴇ schoolswimsuit ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["white", "Gɪᴠᴇ white ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["barefoot", "Gɪᴠᴇ barefoot ᴀɴɪᴍᴀᴛɪᴏɴ."],
       ["touhou", "Give touhou animation."],
       ["gamecg", "Give gamecg animation."],
       ["hololive", "Give hololive animation."],
       ["uncensored", "Give uncensored animation."],
       ["sunglasses", "Give sunglasses animation."],
        ],
                                         )
