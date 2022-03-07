from .. import Riz, SUDO_USERS
from .. import ALIVE_PIC else "https://telegra.ph/file/fddc917e2b37dabf21282.jpg"
from telethon import events
from time import time
from datetime import datetime

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)

RIZ_PIC = ALIVE_PIC    
            
@Riz.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SMEX_USERS:
     await e.reply(text, parse_mode=None, link_preview=None )
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption="✧ Scythe Userbot is alive !! ✧\n\n ┏━━━━━━━━━━━━━━━━━━━\n ┣➣ ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 3.9.6\n ┣➣ ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ : 1.17\n ┣➣ "                               
                              )
