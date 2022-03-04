import os

OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_SECRET = os.getenv('OAUTH_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
TWITTER_HANDLE = os.getenv('TWITTER_HANDLE')
DATABASE_URL_WORKING = os.getenv('DATABASE_URL_WORKING')
COUNT_PER_ROUND = int(os.getenv('COUNT_PER_ROUND'))
USERS_PER_ROUND = int(os.getenv('USERS_PER_ROUND'))
MAX_SECCONDS = int(os.getenv('MAX_SECCONDS'))
MESSAGE = os.getenv('MESSAGE')
TAG = os.getenv('TAG')
