import os

# acquired at https://github.com/settings/tokens
TOKEN = os.getenv('GH_AUTH')
APP_PORT = int(os.getenv('PORT', 8080))
