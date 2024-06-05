import asyncio

from prettytable import PrettyTable
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from config import SUDO_USERS

from X import app, CMD_HELP
from X.helpers.cmd import *
from X.helpers.PyroHelpers import ReplyCheck
from X.helpers.utility import split_list


async def edit_or_reply(message: Message, *args, **kwargs) -> Message:
    xyz = (
        message.edit_text
        if bool(message.from_user and message.from_user.is_self or message.outgoing)
        else (message.reply_to_message or message).reply_text
    )
    return await xyz(*args, **kwargs)

@Client.on_message(
    filters.command(["help", "helpme"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def module_help(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="helper")
            await asyncio.gather(
                message.delete(),
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")
            ac = PrettyTable()
            ac.header = False
            ac.title = "𝐒𝐇𝐔𝐁𝐇-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐏𝐋𝐔𝐆𝐈𝐍𝐒"
            ac.align = "l"
            for x in split_list(sorted(CMD_HELP.keys()), 2):
                ac.add_row([x[0], x[1] if len(x) >= 2 else None])
            xx = await client.send_message(
                message.chat.id,
                f"```{str(ac)}```\n• Mᴏᴅᴜʟᴇꜱ Pʀᴏᴠɪᴅᴇᴅ Bʏ 𝐒𝐡𝐮𝐛𝐡-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓•",
                reply_to_message_id=ReplyCheck(message),
            )
            await xx.reply(
                f"**Usage:** `.help broadcast` **To View Module Information**"
            )
            return

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"──「 **Help For {str(help_arg).upper()}** 」──\n\n"
            for x in commands:
                this_command += f"  •  **Command:** `.{str(x)}`\n  •  **Function:** `{str(commands[x])}`\n\n"
            this_command += "Mᴏᴅᴜʟᴇꜱ Pʀᴏᴠɪᴅᴇᴅ Bʏ 𝐒𝐡𝐮𝐛𝐡-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 "
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"`{help_arg}` **Not a Valid Module Name.**",
            )


@Client.on_message(
    filters.command(["plugins", "modules"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def module_helper(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif message.reply_to_message and len(cmd) == 1:
        help_arg = message.reply_to_message.text
    elif not message.reply_to_message and len(cmd) == 1:
        ac = PrettyTable()
        ac.header = False
        ac.title = "𝐒𝐡𝐮𝐛𝐡-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐏𝐋𝐔𝐆𝐈𝐍𝐒"
        ac.align = "l"
        for x in split_list(sorted(CMD_HELP.keys()), 2):
            ac.add_row([x[0], x[1] if len(x) >= 2 else None])
        await edit_or_reply(
            message, f"```{str(ac)}```\n• @Mrpasserby_1227 × Mᴏᴅᴜʟᴇꜱ Pʀᴏᴠɪᴅᴇᴅ Bʏ 𝐒𝐡𝐮𝐛𝐡-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 •"
        )
        await message.reply(
            f"**Usage**:`.help broadcast` **To View Module details**"
        )

    if help_arg:
        if help_arg in CMD_HELP:
            commands: dict = CMD_HELP[help_arg]
            this_command = f"──「 **Help For {str(help_arg).upper()}** 」──\n\n"
            for x in commands:
                this_command += f"  •  **Command:** `.{str(x)}`\n  •  **Function:** `{str(commands[x])}`\n\n"
            this_command += "Mᴏᴅᴜʟᴇꜱ Pʀᴏᴠɪᴅᴇᴅ Bʏ 𝐒𝐡𝐮𝐛𝐡-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓"
            await edit_or_reply(
                message, this_command, parse_mode=enums.ParseMode.MARKDOWN
            )
        else:
            await edit_or_reply(
                message,
                f"`{help_arg}` **Not a Valid Module Name.**",
            )


def add_command_help(module_name, commands):
    if module_name in CMD_HELP.keys():
        command_dict = CMD_HELP[module_name]
    else:
        command_dict = {}

    for x in commands:
        for y in x:
            if y is not x:
                command_dict[x[0]] = x[1]

    CMD_HELP[module_name] = command_dict 
