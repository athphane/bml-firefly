import ast
import logging
import os
import sys
from configparser import ConfigParser
from logging.handlers import TimedRotatingFileHandler

from aiobml import asyncBML
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from bmlfireflybot.bmlfireflybot import BmlFireflyBot

# Created logs folder if it is not there. Needed for logging.
if not os.path.exists('logs'):
    os.makedirs('logs')

# Logging at the start to catch everything
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y/%m/%d %I:%M:%S %p',
    level=logging.WARNING,
    handlers=[
        TimedRotatingFileHandler(f"logs/{BmlFireflyBot.__name__.lower()}.log", when="midnight", encoding=None,
                                 delay=False, backupCount=10),
        logging.StreamHandler()
    ]
)
LOGS = logging.getLogger(__name__)

__version__ = '1.0.0'
__author__ = 'athphane'

BmlFireflyBot = BmlFireflyBot(__version__)

# Read from config file
name = str(BmlFireflyBot).lower()
config_file = f"{name}.ini"
config = ConfigParser()
config.read(config_file)

# Get from config file.
ADMINS = ast.literal_eval(config.get(name, 'admins'))
LOG_GROUP = config.get(name, 'log_group', fallback=None)

try:
    BOT_USERNAME = config.get(name, 'bot_username')
except:
    print("BOT USERNAME IS REQUIRED. ADD TO CONFIG FILE")
    sys.exit()

MONGO_URL = config.get('mongo', 'url')
DB_NAME = config.get('mongo', 'db_name')
DB_USERNAME = config.get('mongo', 'db_username')
DB_PASSWORD = config.get('mongo', 'db_password')

BML_USERNAME = config.get('bml', 'username')
BML_PASSWORD = config.get('bml', 'password')

FIREFLY_TOKEN = config.get('firefly', 'token')

# Global Variables
client = None

scheduler = AsyncIOScheduler()

bank = asyncBML(username=BML_USERNAME, password=BML_PASSWORD)
