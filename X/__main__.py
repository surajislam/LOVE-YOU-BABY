#MIT License

#Copyright (c) 2024 Japanese-X-Userbot

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import importlib
from pyrogram import idle
from uvloop import install


from X.modules import ALL_MODULES
from X import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids, bot1
from X.helpers import join
from X.helpers.misc import create_botlog, heroku

BOT_VER = "4.0.0"
CMD_HANDLER = ["." "?" "!" "*"]
MSG_ON = """
✧✧ **𝐒IMPLE-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄** ✧✧
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
✧✧ **𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 -** `{}`
✧✧ **𝐓𝐲𝐩𝐞** **.𝐚𝐥𝐢𝐯𝐞** **𝐭𝐨 𝐂𝐡𝐞𝐜𝐤 𝐁𝐨𝐭**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    print("𝐋𝐎𝐆: 𝐅𝐨𝐮𝐧𝐝𝐞𝐝 𝐁𝐨𝐭 𝐭𝐨𝐤𝐞𝐧 𝐁𝐨𝐨𝐭𝐢𝐧𝐠..")
    for all_module in ALL_MODULES:
        importlib.import_module("X.modules" + all_module)
        print(f"𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐈𝐦𝐩𝐨𝐫𝐭𝐞𝐝 {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            except BaseException:
                pass
            print(f"𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐚𝐬 {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("X").info("𝐒IMPLE-𝐗-𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐈𝐬 𝐀𝐜𝐭𝐢𝐯𝐞✨")
    install()
    heroku()
    LOOP.run_until_complete(main())
