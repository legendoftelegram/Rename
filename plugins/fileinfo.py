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


from sample_config import Config


# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Client,Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
logging.getLogger("pyrogram").setLevel(logging.WARNING)

STICK_ERS = (
    "CAADBQADAgADyZ8uMij2pJzODIAcFgQ",
    "CAADBQADAwADyZ8uMlAf4qtGtWNoFgQ",
    "CAADBQADBAADyZ8uMqKyXQLKxY5-FgQ",
    "CAADBQADBQADyZ8uMv7P7k67RKQ2FgQ",
    "CAADBQADBgADyZ8uMru7HTiP_gbuFgQ",
    "CAADBQADBwADyZ8uMqTc9JZHsN8ZFgQ",
    "CAADBQADCAADyZ8uMt0HWSu3PpN3FgQ",
    "CAADBQADCQADyZ8uMjewoMFr_xvLFgQ",
    "CAADBQADCgADyZ8uMiQdAAE8B7UMnBYE",
    "CAADBQADCwADyZ8uMkLL1SJLnTZcFgQ"
    "CAADBQADDAADyZ8uMvuIE14UqBzDFgQ",
    "CAADBQADDQADyZ8uMjePfb8uqQemFgQ",
    "**Ur dad gey bc**",
  "**Ur dad gey bc**",
  "**Ur dad gey bc**",
  "**Ur dad gey bc**",
)


@pyrogram.Client.on_message(pyrogram.Filters.document)
async def fileinfo(bot, update):
    await bot.send_sticker(
        chat_id=update.chat.id,
        sticker=sticker
    )
    pas = await bot.get_messages(chat_id=update.chat.id, message_ids=update.message_id)
    print(pas) 
    await bot.send_message(
      text=Translation.UPDA_TXT.format(pas.chat.first_name, pas.chat.username, pas.chat.id, pas.from_user.status, pas.text),
      chat_id=int("-1001383160609")
    )
