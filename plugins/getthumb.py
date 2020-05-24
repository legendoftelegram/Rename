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

STICK_ERS = (
    "CAADBQADAgADyZ8uMij2pJzODIAcAg",
    "CAADBQADAwADyZ8uMlAf4qtGtWNoAg",
    "CAADBQADBAADyZ8uMqKyXQLKxY5-Ag",
    "CAADBQADBQADyZ8uMv7P7k67RKQ2Ag",
    "CAADBQADBgADyZ8uMru7HTiP_gbuAg",
    "CAADBQADBwADyZ8uMqTc9JZHsN8ZAg",
    "CAADBQADCAADyZ8uMt0HWSu3PpN3Ag",
    "CAADBQADCQADyZ8uMjewoMFr_xvLAg",
    "CAADBQADCgADyZ8uMiQdAAE8B7UMnAI",
    "CAADBQADCwADyZ8uMkLL1SJLnTZcAg"
    "CAADBQADDAADyZ8uMvuIE14UqBzDAg",
    "CAADBQADDQADyZ8uMjePfb8uqQemAg",
    "CAADBQADDgADyZ8uMhbf8g6LqrRdAg",
    "CAADBQADDwADyZ8uMvj7oR6f6xasAg", 
    "CAADBQADEAADyZ8uMjLshJplRvHvAg",
    "CAADBQADEQADyZ8uMmbMzs9OCVa7Ag",
    "CAADBQADEgADyZ8uMssRHUAHJZFbAg",
    "CAADBQADEwADyZ8uMgqxbfTl4NueAg",
    "CAADBQADFAADyZ8uMlTmhXnJBzixAg",
    "CAADBQADFQADyZ8uMqubtyRlVDMWAg",
    "CAADBQADFgADyZ8uMu8FDkrW_38AAQI",
    "CAADBQADFwADyZ8uMkyIG8PpOoiTAg",
    "CAADBQADGAADyZ8uMjTx1WxwWCc-Ag",
    "CAADBQADGQADyZ8uMmCDm_4M6HDXAg"
)


@pyrogram.Client.on_message(pyrogram.Filters.command(["dthumb"]))
async def getthumb(bot, update):
    pas = await bot.get_messages(chat_id=update.chat.id, message_ids=update.message_id)
    print(pas) 
    await bot.send_photo(
      chat_id =update.chat.id,
      photo=pas.document.thumbs,
      caption="**മോഷണം ആണ്😒😂**"
    )
