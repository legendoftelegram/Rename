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
from sample_config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)



@pyrogram.Client.on_message(pyrogram.Filters.document)
async def getchat(bot, update):
    out = await bot.get_messages(chat_id=update.chat.id, message_ids=update.message_ids)
    print(out) 
    await bot.send_message(
      text=Translation.USER_TXT.format(out.id, out.type, out.is_verified, out.is_restricted, out.is_scam, out.is_support, out.first_name, out.last_name, out.username),
      chat_id=update.chat.id
    )
