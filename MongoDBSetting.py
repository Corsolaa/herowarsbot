# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 17/05/2022
# * * * * * * * * * * * *
from pymongo import MongoClient
cluster = MongoClient(open("text_files/mongoDBToken.txt", "r").read())
db = cluster["crosswar"]
collection = db["crosswarcol"]
collectionEm = db["crosswaremoji"]
