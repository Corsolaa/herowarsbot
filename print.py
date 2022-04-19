# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 19/04/2022
# * * * * * * * * * * * *
from MongoDBSetting import collection
from structures import structures


def gc_print():
    retMes = "No assignments set..."
    for i in collection.find({}, {"_id": 0, "playerID": 1, "place": 1, "spot": 1}):
        playerID = str(i["playerID"])
        placeKey = str(i["place"])
        spot = str(i["spot"])
        structures[placeKey][2][spot] = playerID
        retMes = []
    for j in structures:
        if structures[j][2]:
            breakMes = "---------------"
            city = f"**--{structures[j][0].upper()}--**"
            retMes.append(city)
            for l in structures[j][2]:
                retMes.append(f"{l}: {structures[j][2][l]}")
            retMes.append(breakMes)
    return retMes
