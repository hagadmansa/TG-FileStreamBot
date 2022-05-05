import asyncio
import urllib.parse
import logging
from pyrogram import filters
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot
from WebStreamer.utils import get_hash, get_name
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio), group=4,)
async def media_receive_handler(b, m: Message):
    log_msg = await b.copy_message(chat_id=Var.BIN_CHANNEL, from_chat_id=m.chat.id, message_id=m.message_id)
    stream_link = f"{Var.URL}/{log_msg.message_id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
    short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.message_id}"
    logging.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    
    await log_msg.reply_text(
            text=f"😎 Hello Himanshu, i generated a link for **{m.from_user.mention(style='md')}**. You can view **{m.from_user.mention(style='md')}'s** all generated links with **#u{m.chat.id}**.",
            quote=True,
            parse_mode="markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📥 Stream link', url=short_link)
                    ]
                ]
            )
    )
    
    await m.reply_text(
        text="""<b>🤓 Just reply this file with /link to generate an extra link.</b>""",
        quote=True,
        parse_mode="html",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📥 Stream link', url=short_link)
                    ]
                ]
            )
        )
    
#@StreamBot.on_message(filters.channel & (filters.document | filters.video) & ~filters.edited, group=-1)
async def channel_receive_handler(bot, broadcast):
    
    try:
        log_msg = await broadcast.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}/{log_msg.message_id}/{quote_plus(get_name(broadcast))}?hash={get_hash(log_msg)}"
        short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.message_id}"
        
        await log_msg.reply_text(
            text=f"😍 Hello Himanshu, this file has been sent from **{broadcast.chat.title}**. You can view **{broadcast.chat.title}'s** all generated links with **#{broadcast.chat.id}**.".replace('-', 'c'),
            quote=True,
            parse_mode="markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📥 Full link', url=stream_link),
                        InlineKeyboardButton('📦 Short link', url=short_link)
                    ]
                ]
            )
        )
        await bot.edit_message_reply_markup(
            chat_id=broadcast.chat.id,
            message_id=broadcast.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📥 Full link', url=stream_link),
                        InlineKeyboardButton('📦 Short link', url=short_link)
                    ]
                ]
            )
        )
    except Exception as e:
        await bot.send_message(chat_id=Var.BIN_CHANNEL, text=f"#error <code>{e}</code>",
                               disable_web_page_preview=True,
                               parse_mode="HTML")
        print(f"Can't edit broadcast message \n Error: {e}")
        
        
