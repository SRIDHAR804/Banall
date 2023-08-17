import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "13399054"))
    API_HASH = os.environ.get("API_HASH", "585801d590dac4c79aeaa7bcda495e62")
     = os.environ.get("BOT_TOKEN", "5753462185:AAGfUMEZKVA3fH_EHGttXroE1MM9eXy5Pao")
