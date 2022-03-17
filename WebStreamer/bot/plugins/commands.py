from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command('instructions'))
async def command(b, m:Message):
    await m.reply_text(
        text="""Test command""",
    )
