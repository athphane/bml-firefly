from pyrogram.types import Message

from bmlfireflybot.bmlfireflybot import BmlFireflyBot
from bmlfireflybot.utils import custom_filters


@BmlFireflyBot.on_message(custom_filters.group)
async def fuck_groups(_, message: Message):
    """
     Needed to plop this somewhere
    """
    message.stop_propagation()
