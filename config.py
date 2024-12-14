from os import environ

API_ID = int(environ.get("API_ID", "24482734"))
API_HASH = environ.get("API_HASH", "5ccf6a58166cc047a7eba01c5dbc930c")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001891110437"))
ADMINS = int(environ.get("ADMINS", "1790775725"))
DB_URI = environ.get("DB_URI", "mongodb+srv://hnyx:wywyw2@cluster0.9dxlslv.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = environ.get("DB_NAME", "lcujoinrequetbot")
