# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start"]))
async def start(_, m: Message):
    await m.reply(
        text="👋 Hello {m.from_user.mention(style="md")}, send me a file to get an instant link",
        reply_markup=InlineKeyboardMarkup(
                        [[
                          InlineKeyboardButton("📡 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")],
                         [InlineKeyboardButton("🔄 Refresh / Try Again", url=f"https://t.me/{(await b.get_me()).username}?start={usr_cmd}")
                        
                        ]]
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
