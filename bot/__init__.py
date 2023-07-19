import logging
import os
import time
import random
import string
import subprocess
import requests

import telegram.ext as tg
from dotenv import load_dotenv

from telegraph import Telegraph

botStartTime = time.time()
if os.path.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

load_dotenv('config.env')

def getConfig(name: str):
    return os.environ[name]

LOGGER = logging.getLogger(__name__)

try:
    if bool(getConfig('_____REMOVE_THIS_LINE_____')):
        logging.error('The README.md file there to be read! Exiting now!')
        exit()
except KeyError:
    pass

BOT_TOKEN = None

AUTHORIZED_CHATS = set()

AUTHORIZED_CHATS = set()
if os.path.exists('authorized_chats.txt'):
    with open('authorized_chats.txt', 'r+') as f:
        lines = f.readlines()
        for line in lines:
            AUTHORIZED_CHATS.add(int(line.split()[0]))
try:
    achats = getConfig('AUTHORIZED_CHATS')
    achats = achats.split(" ")
    for chats in achats:
        AUTHORIZED_CHATS.add(int(chats))
except:
    pass

try:
    BOT_TOKEN = getConfig('BOT_TOKEN')
    OWNER_ID = int(getConfig('OWNER_ID'))
except KeyError as e:
    LOGGER.error("One or more env variables missing! Exiting now")
    exit(1)

# Generate Telegraph Token
sname = ''.join(random.SystemRandom().choices(string.ascii_letters, k=8))
LOGGER.info("Generating TELEGRAPH_TOKEN using '" + sname + "' name")
telegraph = Telegraph()
telegraph.create_account(short_name=sname)
telegraph_token = telegraph.get_access_token()

DRIVE_NAME = []
DRIVE_ID = []
INDEX_URL = []

try:
    TOKEN_PICKLE_URL = getConfig('TOKEN_PICKLE_URL')
    if len(TOKEN_PICKLE_URL) == 0:
        TOKEN_PICKLE_URL = None
    else:
        out = subprocess.run(["wget", "-q", "-O", "token.pickle", TOKEN_PICKLE_URL])
        if out.returncode != 0:
            logging.error(out)
except KeyError:
    TOKEN_PICKLE_URL = None
try:
    DRIVE_FOLDER_URL = getConfig('DRIVE_FOLDER_URL')
    if len(DRIVE_FOLDER_URL) == 0:
        DRIVE_FOLDER_URL = None
    else:
        out = subprocess.run(["wget", "-q", "-O", "drive_folder", DRIVE_FOLDER_URL])
        if out.returncode != 0:
            logging.error(out)
except KeyError:
    DRIVE_FOLDER_URL = None

if os.path.exists('drive_folder'):
    with open('drive_folder', 'r+') as f:
        lines = f.readlines()
        for line in lines:
            temp = line.strip().split()
            DRIVE_NAME.append(temp[0].replace("_", " "))
            DRIVE_ID.append(temp[1])
            try:
                INDEX_URL.append(temp[2])
            except IndexError as e:
                INDEX_URL.append(None)

if not DRIVE_ID:
    LOGGER.error("The README.md file there to be read! Exiting now!")
    exit(1)

updater = tg.Updater(token=BOT_TOKEN, use_context=True)
bot = updater.bot
dispatcher = updater.dispatcher
