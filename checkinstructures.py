from structures import structures


def checkStructures():
    retMes = []
    for j in structures:
        retMes.append(f"**--{structures[j][0].lower()}--**")
    retMes.append("---------------")

    return retMes
