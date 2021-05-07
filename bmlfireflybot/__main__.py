import bmlfireflybot
from bmlfireflybot import BmlFireflyBot, scheduler

if __name__ == '__main__':
    bmlfireflybot.client = BmlFireflyBot

    scheduler.start()

    BmlFireflyBot.run()
