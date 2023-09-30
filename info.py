import re
from os import environ
import os
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'LazyPrincess')
API_ID = int(environ.get('API_ID', '15917107'))
API_HASH = environ.get('API_HASH', '8197e7638d58c92ae2504adba7c62117')
BOT_TOKEN = environ.get('BOT_TOKEN', "5736646811:AAHXmO-XoV5llwCm4c4q3AFaH2mGi5wCRxI")

#Port
PORT = environ.get("PORT", "8080")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', true))
PICS = (environ.get('PICS', 'https://telegra.ph/file/68d28011b2bc356b5db01.png')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1503578112').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '--1001772308598').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1503578112').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '-1001772308598')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "ac-sewzi7d-shard-00-02.uktjav1.mongodb.net")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
def is_enabled(value):
    return value.lower() in ['1', 'true', 'yes', 'on']


single_button_env = os.environ.get('SINGLE_BUTTON', 'True')


SINGLE_BUTTON = is_enabled(single_button_env)
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '--1001930977544')            
                  

      # URL Shortener #

URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'api.shareus.in/shortLink')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '')

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 100))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True

    # Download Tutorial Button #
DOWNLOAD_TEXT_NAME = "📥 HOW TO DOWNLOAD 📥"
DOWNLOAD_TEXT_URL = "https://t.me/+9hpzSIMAO_YyYjU9"

   # Custom Caption Under Button #
CAPTION_BUTTON = "Get Updates"
CAPTION_BUTTON_URL = "https://t.me/+OuAZLyysqzo4YWY1"

   # Auto Delete For Bot Sending Files #
