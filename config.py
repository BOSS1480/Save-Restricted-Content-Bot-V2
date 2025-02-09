# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22558238"))
API_HASH = getenv("API_HASH", "41abc14dd9f760887a50f9cd2cc1bb73")
BOT_TOKEN = getenv("BOT_TOKEN", "7780733128:AAFFWua36Pul4Ozsw7X8bsBTnO7KpQkIims")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6335855540").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://y0534150646:330833039@cluster0.ysd9p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002410900574")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002220810746"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "1"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "af49ba11b489e6c451ea5d33bc7987b1808d83fd")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
