import time
import os
from bmlfireflybot.utils import custom_filters
from bmlfireflybot.bmlfireflybot import BmlFireflyBot
from pyrogram.types import Message


@BmlFireflyBot.on_message(custom_filters.command('log'))
async def send_log_file(bot: BmlFireflyBot, message: Message):
    if os.path.exists(f"logs/{BmlFireflyBot.__name__.lower()}.log"):
        await message.reply_chat_action('upload_document')
        await message.reply_document(
            document=f"logs/{BmlFireflyBot.__name__.lower()}.log",
            caption="This file was uploaded on:\n**{}**".format(time.ctime(time.time()))
        )
    else:
        await message.reply("Oddly enough, there is no log file. Try again?")



