from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command('start'))
async def command(b, m:Message):
    await m.reply_text(
        text="""👋 Hello {},
        
🤖 My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.

🧐 Don't know how to do? No worries, just press the help button.

👨‍💻 My Creator is <a href=https://t.me/hagadmansa>Hagadmansa</a>.""".format(m.from_user.mention),
        reply_markup=InlineKeyboardMarkup
        ([[
            InlineKeyboardButton('🌐 Website', url='https://hagadmansa.com'),
            InlineKeyboardButton('📣 Updates', url='https://t.me/hagadmansa')
            ],[
            InlineKeyboardButton('ℹ️ Help', callback_data='help'),
            InlineKeyboardButton('😊 About', callback_data='about')
        ]]),
        disable_web_page_preview=True,
    )
      
     
@StreamBot.on_message(filters.command('help'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>ℹ️ HELP</b>
        
Here is the list of my commands, please read carefully everything. if anything happened to you then we are not responsible.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❓ How to use me', callback_data='howtouseme')
            ],[
            InlineKeyboardButton('⚙️ Instructions', callback_data='instructions'),
            InlineKeyboardButton('🕹 Tutorials', callback_data='tutorials'),
            ],[
            InlineKeyboardButton('🔙 Back', callback_data='home'),
            InlineKeyboardButton('📣 Channel', url='https://t.me/hagadmansa')
        ]]
    ),
        disable_web_page_preview=True,
    )
