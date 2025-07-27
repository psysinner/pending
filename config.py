from dotenv import load_dotenv
from os import environ
import os

# Load environment variables from .env file
load_dotenv()

API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", ""))

DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

NEW_REQ_MODE = environ.get("NEW_REQ_MODE", "False").lower() == "true"
