# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 19/04/2022
# * * * * * * * * * * * *
from helpdesk import gc_allassign_help


def gc_unassign(build=None, ):
    retMes = gc_allassign_help("uas", 0x03ecfc)
    if build == "help":
        return retMes
    return retMes
