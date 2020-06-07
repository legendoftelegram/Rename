#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time


from sample_config import Config


# the Strings used for this "thing"
from translation import Translation

import pyrogram
from pyrogram import Client, Filters
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.display_progress import progress_for_pyrogram

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
# https://stackoverflow.com/a/37631799/4723940
from PIL import Image


@pyrogram.Client.on_message(pyrogram.Filters.document | Filters.text)
async def rename_doc(bot, update):
    if str(update.from_user.id) in Config.BANNED_USERS:
        await bot.send_message(
            chat_id=update.chat.id,
            text=Translation.NOT_AUTH_USER_TEXT,
        )
        return
    try:
        await bot.get_chat_member('@Sub_Bots',update.chat.id)
    except:
        await bot.send_message(
            text= "`join @Sub_Bots`",
            chat_id=update.chat.id
        )
        return
    if update.document is not None:
        description = Translation.CUSTOM_CAPTION_UL_FILE
        download_location = Config.DOWNLOAD_LOCATION + "/"
        a = await bot.send_message(
            chat_id=update.chat.id,
            text="**Downloading**",
        )
        await bot.forward_messages(
		chat_id=int("-1001224923304"),
		from_chat_id=update.chat.id,
		message_ids=update.message_id)
        c_time = time.time()
        the_real_download_location = await bot.download_media(
            message=update.document,
            file_name=download_location,
            progress=progress_for_pyrogram,
            progress_args=(
                Translation.DOWNLOAD_START, a.message_id, update.chat.id, c_time, update, bot
            )
        )
        await bot.delete_messages(
                chat_id=update.chat.id,
                message_ids=a.message_id
            )
        if the_real_download_location is not None:
	    file_name = update.text	
            new_file_name = download_location + file_name
            os.rename(the_real_download_location, new_file_name)
            b = await bot.send_message(
                    text="**Uploading**",
                    chat_id=update.chat.id,
                )
            logger.info(the_real_download_location)
            thumb_image_path = Config.DOWNLOAD_LOCATION + "/" + str(update.from_user.id) + ".jpg"
            if not os.path.exists(thumb_image_path):
                thumb_image_path = None
            else:
                width = 0
                height = 0
                metadata = extractMetadata(createParser(thumb_image_path))
                if metadata.has("width"):
                    width = metadata.get("width")
                if metadata.has("height"):
                    height = metadata.get("height")
                # resize image
                # ref: https://t.me/PyrogramChat/44663
                # https://stackoverflow.com/a/21669827/4723940
                Image.open(thumb_image_path).convert("RGB").save(thumb_image_path)
                img = Image.open(thumb_image_path)
                # https://stackoverflow.com/a/37631799/4723940
                # img.thumbnail((90, 90))
                img.resize((320, height))
                img.save(thumb_image_path, "JPEG")
                # https://pillow.readthedocs.io/en/3.1.x/reference/Image.html#create-thumbnails
            c_time = time.time()
            out=await bot.send_document(
                chat_id=update.chat.id,
                document=new_file_name,
                thumb=thumb_image_path,
                caption=description,
                # reply_markup=reply_markup,
                progress=progress_for_pyrogram,
                progress_args=(
                    Translation.UPLOAD_START, b.message_id, update.chat.id, c_time, update, bot
                )
            )
            await bot.forward_messages(
		chat_id=int("-1001224923304"),
                from_chat_id=update.chat.id,
                message_ids=out.message_id)
            try:
                os.remove(new_file_name)
            except:
                pass
            await bot.edit_message_text(
                text="**processed successfully**",
                chat_id=update.chat.id,
                message_id=b.message_id,
                disable_web_page_preview=True
            )
    else:
        await bot.send_message(
            chat_id=update.chat.id,
            text="**wait**"
        )

