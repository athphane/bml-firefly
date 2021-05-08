> This project is in no way associated with Bank of Maldives (hereafter referred to as BML).
> Use this project at your own risk. The author claims no responsibility on what may happen to a user's 
> bank account from the usage of this project. 
---
# BML Firefly Integration Bot
A Telegram Bot based on [Pyrogram](https://github.com/pyrogram/pyrogram) to help auto add transactions to a 
[Firefly-III](https://github.com/firefly-iii/firefly-iii) instance.


## Requirements
You're gonna need to get the following programs and services either installed on your server
or signed up for. You must do all. It is a cardinal sin if you don't.

* `virtualenv` installed so that the packages don't interfere with other system packages.

* [MongoDB](https://www.mongodb.com) on your server or a free server from 
[MongoDB Atlas](https://www.mongodb.com/cloud/atlas). (I recommend Atlas as I used it during
development with no issues.)

## Installing
```bash
git clone https://github.com/athphane/bml-firefly.git
cd bml-firefly
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python -m bmlfireflybot
```

## Developing
To add extra modules to the bot, simply add the code into [bmlfireflybot/plugins](bmlfireflybot/plugins). Each file
that is added to the 'plugins' directory should have the following code at a minimum.

```python
from pyrogram.types import Message
from bmlfireflybot.utils import custom_filters

from bmlfireflybot import BmlFireflyBot


@BmlFireflyBot.on_message(custom_filters.command('sample', ['.']))
async def module_name(bot: BmlFireflyBot, message: Message):
    await message.edit("This is a sample module")
```

This example is only for Pyrogram on_message events. 
