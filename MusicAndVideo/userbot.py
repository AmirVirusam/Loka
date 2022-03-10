import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("Week", 60 * 60 * 24 * 7),
    ("Day", 60 * 60 * 24),
    ("Hour", 60 * 60),
    ("Minutes", 60),
    ("Seconds", 1),
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return " , ".join(parts)

@Client.on_message(filters.command(["ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>⚡ Ping</b> - **{delta_ping * 100:.3f} ms** \n<b>☄ UpTime</b> **-** **{uptime}**"
    )

@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ VC Player Restarted . . . !**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["help"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>🌌 Hi Dear {m.from_user.mention} !

🌠 Welcome To Helper Player !

🛸 Commands !

• {HNDLR}play - [ Reply To Music | Link YouTube | Name Music ] 🏖

• {HNDLR}vplay - [ Reply To Video | Link YouTube | Name Video ] 🍁

• {HNDLR}playlist - To View PlayList 🌱

• {HNDLR}ping - To Check Status 🌟

• {HNDLR}resume - To Continue Playing A Song Or Video 🗼

• {HNDLR}pause - To Pause The PlayBack Of A Song Or Video 🍂

• {HNDLR}skip - To Skip Songs Or Videos 🌿

• {HNDLR}end - To End PlayBack 🪴

• {HNDLR}song - [ Link YouTube | Name Music ] 🍃

• {HNDLR}vsong - [ Link YouTube | Name Music ]🌵 


• Developer : @AmirVirusam 👨‍💻</b>
"""
    await m.reply(HELP)
