from pyrogram.types import Message

from bmlfireflybot.bmlfireflybot import BmlFireflyBot
from bmlfireflybot.utils import custom_filters


@BmlFireflyBot.on_message(custom_filters.command("help"))
async def help_message(_, message: Message):
    await message.reply(
        "Here is some helpful information on how to use me! \n"
        "/help - Shows this message\n"
    )
