# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 19/04/2022
# * * * * * * * * * * * *
from helpdesk import gc_allassign_help
from MongoDBSetting import collection
from structures import structures


def gc_unassign(build, name):
    retMes = gc_allassign_help("uas", 0x03ecfc)
    if build == "help":
        return retMes
    if build is not None:
        if build in structures:
            if collection.count_documents({"place": str(build), "playerID": str(name)}) == 1:
                collection.delete_one({"place": str(build), "playerID": str(name)})
                retMes = "done"
                return retMes
            elif collection.count_documents({"place": str(build), "spot": str(name)}) == 1:
                collection.delete_one({"place": str(build), "spot": str(name)})
                retMes = "done"
            else:
                retMes = "failed"
        else:
            print("not a building")
    return retMes
