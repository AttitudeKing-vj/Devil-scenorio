""" Alive module from https://github.com/AnonymousR1025/FallenRobot/blob/55c53a2f37f4062c63265375a7ca19b9a507afcd/FallenRobot/modules/alive.py"""

import os
import re
import random
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from scenario.events import register
from scenario import telethn as tbot
from scenario import SUPPORT_CHAT


PHOTO = [
    "https://telegra.ph/file/d2178f99282b79d5ca1b0.jpg",
    "https://telegra.ph/file/ca141ba231e8f7d9686f8.jpg",
    "https://telegra.ph/file/a3b9264ed18f855f0077d.jpg",
    "https://telegra.ph/file/d2178f99282b79d5ca1b0.jpg",
    "https://telegra.ph/file/ca141ba231e8f7d9686f8.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ DevilxAngeL~**\n━━━━━━━━━━━━━━━━━━━\n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [Attitude King](https://t.me/AttitudeKing_vj)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n━━━━━━━━━━━━━━━━━\n\n"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/DevilxAngeLBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", f"https://t.me/{SUPPORT_CHAT}")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

__help__ = """

/alive - Alive status
"""

__mod_name__ = "Alive"
