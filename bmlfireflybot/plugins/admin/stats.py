from pyrogram.types import Message

from bmlfireflybot.database.users import UserDB
from bmlfireflybot.bmlfireflybot import BmlFireflyBot
from bmlfireflybot.utils import custom_filters


@BmlFireflyBot.on_message(custom_filters.command("users"))
async def users_count(bot: BmlFireflyBot, message: Message):
    users = UserDB().all_users().count()
    await message.reply(f"{BmlFireflyBot.__name__} has {users} users.")
