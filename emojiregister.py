from MongoDBSetting import collectionEm
from checkinstructures import checkStructures


def gc_emojiregister(reaction, user):
    no = checkStructures()
    if reaction.message.content not in no:
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
