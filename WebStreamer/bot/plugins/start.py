from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    
@StreamBot.on_message(filters.command(["about"]))
async def start(_, m: Message):
    await m.reply(
        f'follow me on telegram <a href="https://hagadmansa.com/telegram/">here</a>.'
    )
   
@StreamBot.on_message(filters.command('start'))
async def command(b, m:Message):
    await m.reply_text(
        text="Your Text",
        reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("📡 Join Updates Channel", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]]
                ),
                parse_mode="markdown"
            )
    )
