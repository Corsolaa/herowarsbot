# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 19/04/2022
# * * * * * * * * * * * *
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://Corsolaa:3buMOjOSXg22xiWX@cluster0.zb9ue.mongodb.net/test")
db = cluster["crosswar"]
collection = db["crosswarcol"]
collectionEm = db["crosswaremoji"]
