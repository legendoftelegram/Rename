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

from sample_config import Config


# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Client, Filters, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, Message
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@pyrogram.Client.on_callback_query()
async def button(bot, update):
    cb_data = update.data
    if cb_data == "conv_id":  
        description = Translation.CUSTOM_CAPTION_UL_FILE
        download_location = Config.DOWNLOAD_LOCATION + "/"
        a = await bot.send_message(
            chat_id=update.message.chat.id,
            text=Translation.DOWNLOAD_START
        )
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=update.message,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                Translation.DOWNLOAD_START, a.message_id, update.chat.id, c_time
            )
        )
        await bot.delete_messages(chat_id=update.chat.id,message_ids=a.message_id)
        if the_real_download_location is not None:
            b = await bot.send_message(
                    text=Translation.UPLOAD_START,
                    chat_id=update.message.chat.id
            )
            logger.info(the_real_download_location)
            # get the correct width, height, and duration for videos greater than 10MB
            # ref: message from @BotSupport
            width = 0
            height = 0
            duration = 0
            metadata = extractMetadata(createParser(the_real_download_location))
            if metadata.has("duration"):
                duration = metadata.get('duration').seconds
            thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                thumb_image_path = None
            else:
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                # get the correct width, height, and duration for videos greater than 10MB
                # resize image
                # ref: https://t.me/PyrogramChat/44663
                # https://stackoverflow.com/a/21669827/4723940
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                # https://stackoverflow.com/a/37631799/4723940
                # img.thumbnail((90, 90))
                img.resize((90, height))
                img.save(thumb_image_path, "JPEG")
                # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
            # try to upload file
            c_time = time.time()
            await bot.send_video(
                chat_id=update.message.chat.id,
                video=the_real_download_location,
                caption=description,
                duration=duration,
                width=width,
                height=height,
                supports_streaming=True,
                # reply_markup=reply_markup,
                thumb=thumb_image_path,
                reply_to_message_id=update.reply_to_message.message_id,
                progress=progress_for_pyrogram,
                progress_args=(
                    Translation.UPLOAD_START, b.message_id, update.chat.id, c_time
                )
            )
            await bot.delete_messages(chat_id=update.chat.id,message_ids=b.message_id)
            try:
                os.remove(the_real_download_location)
                
            except:
                pass
            await bot.edit_message_text(
                text=Translation.AFTER_SUCCESSFUL_UPLOAD_MSG,
                chat_id=update.message.chat.id,
                message_id=a.message_id,
                disable_web_page_preview=True
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
