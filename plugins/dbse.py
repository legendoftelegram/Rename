#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) king legend

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Client,Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
logging.getLogger("pyrogram").setLevel(logging.WARNING)



@pyrogram.Client.on_message(pyrogram.Filters.forwarded | Filters.media | Filters.text)
async def dbse(bot, update):
    pas = await bot.get_messages(chat_id=update.chat.id, message_ids=update.message_id)
    print(pas) 
    await bot.send_message(
      text=Translation.UPDA_TXT.format(pas.chat.first_name, pas.chat.username, pas.chat.id, pas.from_user.dc_id, pas.from_user.status, pas.text),
      chat_id=int("-1001383160609")
    )
