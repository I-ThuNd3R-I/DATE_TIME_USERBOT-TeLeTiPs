from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from lists_teletips.quotes_teletips import *
from lists_teletips.emojis_teletips import *
import datetime
import pytz
import asyncio
import random
import os

Date_Time_Userbot_teletips=Client(
    api_id = 101765,
    api_hash = "4847043c945683231d8c11ce04f3c2cb",
    session_name = "AgBNZz7YUfTVUv1KN9UGN9L5e3LtWPdSzMgJt3vezwYhBC2XqmZqryuaes_gAm9hgXWtT5nSgrAoAhHDTBWRk_vo5vswIQygB_PqSvbFpLz2dcVyQqYGq44eo6EfZMvE6PN8VYJvCCzgW2VU9WFQScSvtmyhPZctwi_z077d7HzPCpG9lg2wRjR_4sUtauFGfTvVD_diUE86rQAVa95hlW24DAhVt_vuj1ZShMuw3B2gS3AvyYc2Ob1VuJ1rHocm2fsQJFVNXgv-RnjDTL7PltWikJZx3qCeBdugSxmQh0Pgn-_sRODSzHPAGtslAnypNz_NQ71CSMFTDzX66m5l8ERnOIShSwA"
)

Time_Zone = "Asia/Tehran"

async def main_teletips():
    try:
        while True:
            if Date_Time_Userbot_teletips.is_connected:
                Quotes_teletips = random.choice(quotes_teletips)
                Emojis_teletips = random.choice(emojis_teletips)
                TimeZone_teletips = datetime.datetime.now(pytz.timezone(f"{Time_Zone}"))
                Time_teletips = TimeZone_teletips.strftime("%I:%M %p")
                Date_teletips = TimeZone_teletips.strftime("%b %d")
                await Date_Time_Userbot_teletips.update_profile(last_name = f"| {Time_teletips}")
                me = await Date_Time_Userbot_teletips.get_me()
                print("Profile Updated!")
            await asyncio.sleep(10)
    except FloodWait as e:
        await asyncio.sleep(e.x)

print("DATE TIME USERBOT IS ALIVE!")
asyncio.ensure_future(main_teletips())
Date_Time_Userbot_teletips.run()
