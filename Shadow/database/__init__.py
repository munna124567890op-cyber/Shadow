from pymongo import MongoClient

import config

JAANdb = MongoClient(config.MONGO_URL)
JAAN = JAANdb["JAANDb"]["JAAN"]


from .chats import *
from .users import *
