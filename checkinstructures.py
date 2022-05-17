# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 17/05/2022
# * * * * * * * * * * * *
from structures import structures


def checkStructures():
    retMes = []
    for j in structures:
        retMes.append(f"**--{structures[j][0].lower()}--**")
    retMes.append("---------------")

    return retMes
