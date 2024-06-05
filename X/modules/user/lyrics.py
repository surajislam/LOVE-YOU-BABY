import aiohttp
from pyrogram import filters, Client
from pyrogram.types import Message
import os
from config import OWNER_ID
from config import SUDO_USERS
from config import CMD_HANDLER as cmd

from .help import *

@Client.on_message(
    filters.command(["lyrics"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def get_lyrics(client: Client, message: Message):
    if len(message.command) != 2:
        await message.reply_text("ᴘʟᴇᴀꜱᴇ ᴜꜱᴇ %𝟸𝟶 ɪɴ ʙᴇᴛᴡᴇᴇɴ ʏᴏᴜʀ ꜱᴏɴɢ ɪғ ɪᴛ'ꜱ ᴍᴏʀᴇ ᴛʜᴇɴ 𝟷 ᴡᴏʀᴅ\nExᴀᴍᴘʟᴇ .ʟʏʀɪᴄꜱ ᴛᴜ%𝟸𝟶ʜᴀɪɴ%𝟸𝟶ᴋᴀʜᴀ")
        return

    question = message.text.split(" ", maxsplit=1)[1]

    lyrics_url = f'https://lyrist.vercel.app/api/{question}'

    async with aiohttp.ClientSession() as session:
        async with session.get(lyrics_url) as request:
            if request.status == 404:
                return await message.reply_text("Lʏʀɪᴄꜱ ɴᴏᴛ ғᴏᴜɴᴅ ғᴏʀ ᴛʜɪꜱ ꜱᴏɴɢ.")

            lyrics_data = await request.json()

            try:
                image = lyrics_data['image']
                lyrics = lyrics_data['lyrics']

                lyrics_file_path = f"{question}_lyrics.txt"  # Use 'question' instead of 'song_name'
                with open(lyrics_file_path, "w", encoding="utf-8") as file:
                    file.write(lyrics)

                await client.send_document(
                    chat_id=message.chat.id,
                    document=lyrics_file_path,
                    caption=f"Lʏʀɪᴄꜱ ғᴏʀ {lyrics_data['title']} by {lyrics_data['artist']}"
                )
                await client.send_photo(
                    chat_id=message.chat.id,
                    photo=image
                )

                os.remove(lyrics_file_path)

            except Exception as e:
                print(str(e))
                pass

add_command_help(
    "•─╼⃝𖠁 Lʏʀɪᴄs",
    [
        ["lyrics", "Gᴇᴛ ʟʏʀɪᴄꜱ ғᴏʀ ᴀ ꜱᴏɴɢ."],
    ],
)
