# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start"]))
async def start(_, m: Message):
    await m.reply(
        f'👋 Hello {m.from_user.mention(style="md")},
        
🤖 My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.
        
🧐 Don't know how to do? No worries, just press the help button.
        
👨‍💻 My Creator is <a href="https://t.me/hagadmansa>Hagadmansa"</a>.'
    )
    
@StreamBot.on_message(filters.command(["about"]))
async def start(_, m: Message):
    await m.reply(
        f'follow me on telegram <a href="https://hagadmansa.com/telegram/">here</a>.'
    )
@StreamBot.on_message(filters.command(["about"]))
async def start(_, m: Message):
    await m.reply(
        f'namste nijbhujhkuhjguhg'
    )
