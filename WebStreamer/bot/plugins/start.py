import urllib.parse
from pyrogram import filters
from WebStreamer.vars import Var
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.utils.database import Database
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """
👋 Hello {},
🤖 My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.
🧐 Don't know how to do? No worries, just press the help button.
👨‍💻 My Creator is <a href=https://t.me/hagadmansa>Hagadmansa</a>."""

HELP_TEXT = """<b>ℹ️ HELP</b>
Here is the list of my commands, please read carefully everything. if anything happened to you then we are not responsible."""

START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🌐 Website', url='https://hagadmansa.com'),
            InlineKeyboardButton('📣 Updates', url='https://t.me/hagadmansa')
            ],[
            InlineKeyboardButton('ℹ️ Help', callback_data='help'),
            InlineKeyboardButton('😊 About', callback_data='about')
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❓ How to use me', callback_data='howtouseme')
            ],[
            InlineKeyboardButton('⚙️ Instructions', callback_data='instructions'),
            InlineKeyboardButton('🕹 Tutorials', callback_data='tutorials'),
            ],[
            InlineKeyboardButton('🔙 Back', callback_data='home'),
            InlineKeyboardButton('📣 Channel', url='https://t.me/hagadmansa')
        ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
         )       

@StreamBot.on_message(filters.command(["start"]))
async def start(_, m: Message):
    await m.reply(
        f'Hi {m.from_user.mention(style="md")}, ✅ Send me a ⏺ file to get ❎ an instant stream link.'
    )

@StreamBot.on_message(filters.private & filters.command(["help"]))
async def start(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=HELP_BUTTONS
    )
