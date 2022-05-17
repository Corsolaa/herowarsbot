# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 17/05/2022
# * * * * * * * * * * * *
from MongoDBSetting import collection
from structures import structures
from helpdesk import gc_allassign_help


def gc_assign(build, spot, user):
    retMes = gc_allassign_help("as", 0xff0019)
    if build == "help":
        return retMes
    if build in structures:
        placeName = str(structures[build][0])
        maxSpot = structures[build][1]
        if maxSpot >= spot > 0:
            if collection.count_documents({"_id": str(placeName) + str(spot)}) == 0:
                if collection.count_documents({"playerID": str(user)}) < 2:
                    post = {"_id": str(placeName) + str(spot),
                            "playerID": str(user),
                            "place": str(build),
                            "spot": str(spot)}
                    collection.insert_one(post)
                    retMes = "Player has successfully been set"
                    return retMes
                else:
                    retMes = "Player ID already set 2 times!!!"
                    return retMes
            else:
                retMes = f"{str(placeName)} on spot {str(spot)} is already occupied..."
                return retMes
        else:
            retMes = f"Spot digit invalid, can only be {maxSpot} maximum on structure: {placeName}!!!"
            return retMes
    return retMes
