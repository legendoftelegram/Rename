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
import random, re

from sample_config import Config


# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Client,Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@pyrogram.Client.on_message(pyrogram.Filters.document)
async def fileinfo(bot, update):
     await bot.send_message(
        chat_id=update.chat.id,
        text="**select**",
        reply_markup=InlineKeyboardMarkup(
           [
              [InlineKeyboardButton("stream", callback_data="conv_id"), InlineKeyboardButton("❌DELETE❌", callback_data="help_del")],
          ]
        )
    )
