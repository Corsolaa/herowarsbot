# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 19/04/2022
# * * * * * * * * * * * *
from MongoDBSetting import collection
from structures import structures
from helpdesk import gc_assign_help


def gc_assign(build, spot, user):
    retMes = gc_assign_help()
    if build == "help":
        return retMes
    if build in structures:
        placeName = str(structures[build][0])
        maxSpot = structures[build][1]
        if maxSpot >= spot > 0:
            if collection.count_documents({"_id": str(placeName) + str(spot)}) == 0:
                if collection.count_documents({"playerID": str(user)}) < 2:
                    retMes = "Player has successfully been set"
                    post = {"_id": str(placeName) + str(spot),
                            "playerID": str(user),
                            "place": str(build),
                            "spot": str(spot)}
                    collection.insert_one(post)
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
