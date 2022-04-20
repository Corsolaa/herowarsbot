from MongoDBSetting import collectionEm
from structures import structures


def gc_emojiregister(reaction, user):
    no = []
    for j in structures:
        no.append(f"**--{structures[j][0].lower()}--**")
    no.append("---------------")
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
