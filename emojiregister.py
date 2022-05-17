# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 17/05/2022
# * * * * * * * * * * * *
from MongoDBSetting import collectionEm
from checkinstructures import checkStructures


def gc_emojiregister(reaction, user):
    if reaction.message.content not in checkStructures():
        ID = collectionEm.count_documents({})
        if reaction.emoji == "✅":
            post = {"_id": ID,
                    "reactMes": reaction.message.content,
                    "bool": True}
            collectionEm.insert_one(post)
            return True
        if reaction.emoji == "❌":
            post = {"_id": ID,
                    "reactMes": reaction.message.content,
                    "bool": False}
            collectionEm.insert_one(post)
            return True
        return False
    return False
