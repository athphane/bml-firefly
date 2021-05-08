from datetime import datetime

from pyrogram.types import User as BaseUser

from bmlfireflybot.database import database


class Transactions:
    def __init__(self):
        self.transactions = database()[self.__class__.__name__.lower()]

    def all_transactions(self):
        users = self.transactions.find()
        return users

    def find_transaction(self, transaction):
        return self.transactions.find_one(transaction)

    def create_transaction(self, transaction_data):
        self.transactions.insert_one(transaction_data)
