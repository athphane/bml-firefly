from datetime import datetime

import requests
from pyrogram import emoji
from pyrogram.types import Message

from bmlfireflybot import bank, FIREFLY_TOKEN
from bmlfireflybot.bmlfireflybot import BmlFireflyBot
from bmlfireflybot.database.transactions import Transactions
from bmlfireflybot.utils import custom_filters


@BmlFireflyBot.on_message(custom_filters.command("transactions"))
@BmlFireflyBot.admins_only
async def transactions(bot: BmlFireflyBot, message: Message):
    await message.reply("Finding new transactions")
    count = 0
    url = 'https://firefly.athfan.com/api/v1/transactions'
    my_bank = await bank.get_history()

    if my_bank:
        for account in my_bank:
            for transaction in my_bank[account]:
                if not Transactions().find_transaction(transaction):
                    count += 1
                    Transactions().create_transaction(transaction)

                    thing = {
                        "transactions": [
                            {
                                "type": "withdrawal",
                                "date": datetime.strptime(transaction['date'][:10], '%d-%m-%Y').isoformat(),
                                "amount": abs(transaction['amount']),
                                "description": f"{transaction['description']} at {transaction['sender']}",
                                "currency_code": "MVR",
                                "category_name": "BML-API",
                                "source_id": 1,
                                "destination_name": transaction['sender'],
                                "notes": "Transaction Created via BML-API Bot"
                            }
                        ]
                    }

                    res = requests.post(
                        url,
                        headers={'Authorization': f"Bearer {FIREFLY_TOKEN}",
                                 'Accept': 'application/json'},
                        json=thing).json()

                    txt = (
                        f"{transaction['description']} at {transaction['sender']}\n"
                        f"{emoji.LINK}: https://firefly.athfan.com/transactions/show/{res['data']['id']}"
                    )

                    await message.reply(txt, disable_web_page_preview=True)

    await message.reply(f"{count} transactions created")
