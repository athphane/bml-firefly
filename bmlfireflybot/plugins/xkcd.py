from pyrogram.types import Message
from bmlfireflybot.bmlfireflybot import BmlFireflyBot
from bmlfireflybot.utils import custom_filters
from bmlfireflybot.utils.aiohttp_helper import AioHttp


@BmlFireflyBot.on_message(custom_filters.command("xkcd"))
async def xkcd_image(bot: BmlFireflyBot, message: Message):
    xkcd = await AioHttp.get_json("https://xkcd.com/info.0.json")
    text = xkcd['title'] + "\n\n" + xkcd['alt']
    await message.reply_photo(xkcd['img'], caption=text)
