from .adminHelpers import *
from .basic import *
from .constants import *
from .expand import *
#from .misc import *
from .interval import *
from .msg_types import *
from .parser import *
from .PyroHelpers import *
from .tools import *
from .utility import *


import os
import sys
from pyrogram import Client


def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "X"])

async def join(client):
    try:
        await client.join_chat("anokhikeduniya")
        await client.join_chat("anokhikeduniya")
        await client.join_chat("anokhikeduniya")
        await client.join_chat("anokhikeduniya")
        await client.join_chat("anokhikeduniya")
        await client.join_chat("anokhikeduniya")
    except BaseException:
        pass
