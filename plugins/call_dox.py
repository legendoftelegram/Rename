#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import json
import math
import os
import shutil
import subprocess
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Client, Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@pyrogram.Client.on_callback_query()
async def button(bot, update):
    cb_data = update.data
    if cb_data == "help_pin":  
        await bot.edit_message_text(
           chat_id=update.message.chat.id,
           message_id=update.message.message_id,
           text=Translation.PIN_MSG,
           reply_markup=InlineKeyboardMarkup(
              [
                   [InlineKeyboardButton("🌀BACK🌀", callback_data="help_back")],
              ]
           ) 
        )
    elif cb_data == "help_del":
        await bot.edit_message_text(
           chat_id=update.message.chat.id,
           message_id=update.message.message_id,
           text=Translation.DEL_MSG,
           reply_markup=InlineKeyboardMarkup(
              [
                   [InlineKeyboardButton("🌀BACK🌀", callback_data="help_back")],
              ]
           ) 
        )
