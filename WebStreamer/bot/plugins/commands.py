import random
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
    
@StreamBot.on_message(filters.command('howtouseme'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>ℹ️ Help</b> > How To Use Me
        
My name is Hagadmansa Mega Bot, I am a member of Hagadmansa family. I can provide you direct download link of any telegram file/media. If you send me any file/media I will give an external download link, you can use that link to download any file outside telegram. My link is supported in any browser.

• Send me any file/media from Telegram.
• I Will provide an external download link for you.
• All links will be permanent and have the fastest speed.

<b>🔞 Warning:</b>

• 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
            ]]
    ),
        disable_web_page_preview=True,
    )
    
@StreamBot.on_message(filters.command('instructions'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>ℹ️ Help</b> > Instructions
        
1. Don't send photos to the bot, send them as a file.
2. Don't send multiple files at a time, send them one by one.

<b>🔞 Warning:</b>

• 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
            ]]
    ),
        disable_web_page_preview=True,
    )

@StreamBot.on_message(filters.command('tutorials'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>ℹ️ Help</b> > Tutorials
        
All tutorials related to Bots, Website, Movies and etc, will be updated here. Till then you can visit my movie website <b>www.hagadmansa.com</b> to watch movies. Don't forget to subscribe my updates channel <b>@hagadmansa</b>.

<b>🔞 Warning:</b>

• 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
            ]]
    ),
        disable_web_page_preview=True,
    )
    
@StreamBot.on_message(filters.command('about'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>😊 About</b>
        
<b>✯ My Name:</b> Hagadmansa Mega Bot
<b>✯ Creator:</b> <a href='https://t.me/hagadmansa'>Hagadmansa</a>
<b>✯ Library:</b> <a href='https://pyrogram.org'>Pyrogram</a>
<b>✯ Language:</b> <a href='https://Python.org'>Python</a>
<b>✯ Database:</b> <a href='https://mongodb.com'>MongoDB</a>
<b>✯ Server:</b> <a href='https://heroku.com'>Heroku</a>
<b>✯ Channel:</b> <a href='https://t.me/hagadmansa'>Hagadmansa</a>
<b>✯ Group:</b> <a href='https://t.me/hagadmansachat'>Hagadmansa Support</a>
<b>✯ Brothers:</b> <a href='https://t.me/hagadmansabot'>Hagadmansa Bot</a>, <a href='https://t.me/hagadmansarobot'>Hagadmansa Robot</a>""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🌐 Visit Our Website', url='https://hagadmansa.com')
            ],[
            InlineKeyboardButton('⭐️ Rating', callback_data='rating'),
            InlineKeyboardButton('❤️ Source', callback_data='source'),
            ],[
            InlineKeyboardButton('🔙 Back', callback_data='home'),
            InlineKeyboardButton('🤝 Donate', callback_data='donate')
        ]]
    ),
        disable_web_page_preview=True,
    )
    
@StreamBot.on_message(filters.command('rating'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>😊 About</b> > Rating
        
I have a public channel a private channel and 3 bots, along with this also I have a website. you can rate and write a review on our public channel and bots.

<b>📣 @hagadmansa</b>

1. Details are <a href='https://t.me/tlgrmcbot?start=hagadmansa'>here</a>
2. Review this channel <a href='https://t.me/tlgrmcbot?start=hagadmansa-review'>here</a>

<b>🤖 @hagadmansabot</b>

1. Details are <a href='https://t.me/tlgrmcbot?start=hagadmansabot'>here</a>
2. Review this bot <a href='https://t.me/tlgrmcbot?start=hagadmansabot-review'>here</a>

<b>🤖 @hagadmansarobot</b>

1. Details are <a href='https://t.me/tlgrmcbot?start=hagadmansarobot'>here</a>
2. Review this bot <a href='https://t.me/tlgrmcbot?start=hagadmansarobot-review'>here</a>

<b>🤖 @hagadmansamegabot</b> 

1. Details are <a href='https://t.me/tlgrmcbot?star=hagadmansamegabot'>here</a>
2. Review this bot <a href='https://t.me/tlgrmcbot?start=hagadmansamegabot-review'>here</a>""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
            ]]
    ),
        disable_web_page_preview=True,
    )

@StreamBot.on_message(filters.command('source'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>😊 About</b> > Source
        
<b>❗️NOTE:</b>

We are not open source yet, if in future we are open our code for everyone then we'll update the source code here.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
            ]]
    ),
        disable_web_page_preview=True,
    )
    
@StreamBot.on_message(filters.command('donate'))
async def command(b, m:Message):
    await m.reply_text(
        text="""<b>😊 About</b> > Donate
        
<b>❗️NOTE:</b>

We are not raising any funds right now, if in future we raise funds then we'll update here.""",
        reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🔙 Back', callback_data='help'),
            InlineKeyboardButton('🏠 Home', callback_data='home')
            ]]
    ),
        disable_web_page_preview=True,
    )
    
@StreamBot.on_message(filters.command('luck'))
async def command(b, m:Message):
    await m.reply_text(
        text=f"{random.choice(Hello)}"
        disable_web_page_preview=True,
    )
    
Hello=["Hello","नमस्ते"]
