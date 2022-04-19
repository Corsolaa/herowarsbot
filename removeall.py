# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 19/04/2022
# * * * * * * * * * * * *
from MongoDBSetting import collection


def gc_removeall():
    x = collection.delete_many({})
    if x.deleted_count == 1:
        add = " document deleted."
    else:
        add = " documents deleted."
    return str(x.deleted_count) + add
