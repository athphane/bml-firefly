import asyncio

from pyrogram.types import Message

from bmlfireflybot.bmlfireflybot import BmlFireflyBot
from bmlfireflybot.utils import custom_filters


@BmlFireflyBot.on_message(custom_filters.command("restart"))
@BmlFireflyBot.admins_only
async def restart(bot: BmlFireflyBot, message: Message):
    await message.reply(f"Restarting {BmlFireflyBot}.")

    if 'p' in message.text and 'g' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(git_update=True, pip=True))
    elif 'p' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(pip=True))
    elif 'g' in message.text:
        asyncio.get_event_loop().create_task(bot.restart(git_update=True))
    else:
        asyncio.get_event_loop().create_task(bot.restart())
