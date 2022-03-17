# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
    
@StreamBot.on_message(filters.command(["about"]))
async def start(_, m: Message):
    await m.reply(
        f'follow me on telegram <a href="https://hagadmansa.com/telegram/">here</a>.'
    )
    
@Client.on_message(filters.command("start") 
async def start(client, message):
        await message.reply(script.START_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)

START_TEXT = """
👋 Hello {},
🤖 My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.
🧐 Don't know how to do? No worries, just press the help button.
👨‍💻 My Creator is <a href=https://t.me/hagadmansa>Hagadmansa</a>."""
