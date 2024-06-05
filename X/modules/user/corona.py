import asyncio
import datetime

from prettytable import PrettyTable
from pyrogram import Client, filters
from config import OWNER_ID
from config import SUDO_USERS
from config import CMD_HANDLER as cmd

from X.helpers.aiohttp_helper import AioHttp

from .help import *

@Client.on_message(
    filters.command(["corona"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def corona_all(client, message):
    try:
        r = await AioHttp().get_json("https://api.rootnet.in/covid19-in/stats/latest")
        data = r["data"]["summary"]
        last_refreshed = r["lastRefreshed"]
        
        ac = PrettyTable()
        ac.header = False
        ac.title = "Global Statistics"
        ac.add_row(["Total Cases", f"{data['total']:,}"])
        ac.add_row(["Cases Today", f"{data['confirmedCasesIndian'] + data['confirmedCasesForeign']:,}"])
        ac.add_row(["Deaths", f"{data['deaths']:,}"])
        ac.add_row(["Deaths Today", "N/A"])
        ac.add_row(["Recovered", f"{data['discharged']:,}"])
        ac.add_row(["Active", f"{data['total'] - data['discharged'] - data['deaths']:,}"])
        ac.add_row(["Critical", "N/A"])
        ac.add_row(["Cases/Million", "N/A"])
        ac.add_row(["Deaths/Million", "N/A"])
        ac.add_row(["Tests", "N/A"])
        ac.add_row(["Tests/Million", "N/A"])
        ac.align = "l"

        await message.edit(f"```{str(ac)}```\nLast updated on: {last_refreshed}")
    except Exception as e:
        await message.edit("`The corona API could not be reached`")
        await asyncio.sleep(3)
        await message.delete()

# Ensure to maintain other functions and imports as per your requirement.

add_command_help(
    "•─╼⃝𖠁 ᴄᴏʀᴏɴᴀ",
    [
        ["corona", "Sᴇɴᴅꜱ ɢʟᴏʙᴀʟ ᴄᴏʀᴏɴᴀ ꜱᴛᴀᴛꜱ: ᴄᴀꜱᴇꜱ, ᴅᴇᴀᴛʜꜱ, ʀᴇᴄᴏᴠᴇʀᴇᴅ, ᴀɴᴅ ᴀᴄᴛɪᴠᴇ ᴄᴀꜱᴇꜱ."],
    ],
)
