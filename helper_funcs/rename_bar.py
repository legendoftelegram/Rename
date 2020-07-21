#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import math
import os
import time

# the secret configuration specific things
from sample_config import Config

# the Strings used for this "thing"
from translation import Translation

userids = []

async def progress_for_upload(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 3.00) > 2.999 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "<code>[{0}{1}]| {2}%</code>\n\n".format(
            ''.join(["◼️" for i in range(math.floor(percentage / 5))]),
            ''.join(["◻️" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))

        tmp = progress + "<b>{}</b> <b>of</b> <b>{}</b>\n<b>Speed:</b> <b>{}/s</b>\n<b>Remaining:</b> <b>{}</b> /Cancel".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n {}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass
