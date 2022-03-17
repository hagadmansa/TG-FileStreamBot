from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command('help'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>ℹ️ HELP</b>
        
Here is the list of my commands, please read carefully everything. if anything happened to you then we are not responsible."""
        reply_markup=InlineKeyboardMarkup
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
