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
        text="START_TXT",
        reply_markup=InlineKeyboardMarkup(
                    [[
            InlineKeyboardButton('🌐 Website', url='https://hagadmansa.com'),
            InlineKeyboardButton('📣 Updates', url='https://t.me/hagadmansa')
            ],[
            InlineKeyboardButton('ℹ️ Help', callback_data='help'),
            InlineKeyboardButton('😊 About', callback_data='about')
        ]]
                ),
        parse_mode="markdown"
    )
    
START_TEXT = """
👋 Hello {},
🤖 My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.
🧐 Don't know how to do? No worries, just press the help button.
👨‍💻 My Creator is <a href=https://t.me/hagadmansa>Hagadmansa</a>."""

HELP_TEXT = """<b>ℹ️ HELP</b>
Here is the list of my commands, please read carefully everything. if anything happened to you then we are not responsible."""

ABOUT_TEXT = """<b>😊 About</b>
<b>✯ My Name:</b> Hagadmansa Mega Bot
<b>✯ Creator:</b> <a href='https://t.me/hagadmansa'>Hagadmansa</a>
<b>✯ Library:</b> <a href='https://pyrogram.org'>Pyrogram</a>
<b>✯ Language:</b> <a href='https://Python.org'>Python</a>
<b>✯ Database:</b> <a href='https://mongodb.com'>MongoDB</a>
<b>✯ Server:</b> <a href='https://heroku.com'>Heroku</a>
<b>✯ Channel:</b> <a href='https://t.me/hagadmansa'>Hagadmansa</a>
<b>✯ Group:</b> <a href='https://t.me/hagadmansachat'>Hagadmansa Support</a>
<b>✯ Brothers:</b> <a href='https://t.me/hagadmansabot'>Hagadmansa Bot</a>, <a href='https://t.me/hagadmansarobot'>Hagadmansa Robot</a>"""

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
     elif update.data == "about":
     await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
         )
