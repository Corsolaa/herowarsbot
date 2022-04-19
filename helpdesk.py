# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 19/04/2022
# * * * * * * * * * * * *
from discord import Embed
from structures import structures
from prefix import prefix


def gc_assign_help():
    retMes = Embed(title=f"__**{prefix}AS HELP DESK:**__",
                   description=prefix + "as {structs} {spot} {playername}", color=0x52FF00)
    structsKey = ""
    structsName = ""
    spots = ""
    for x in structures:
        structsKey += f"᲼᲼**{x}**\n"
        structsName += f"*({str(structures[x][0])})*\n"
        spots += f"*1 - {str(structures[x][1])}*\n"
    retMes.add_field(name="STRUCTS", value=structsKey, inline=True)
    retMes.add_field(name="᲼", value=structsName, inline=True)
    retMes.add_field(name="SPOTS", value=spots, inline=True)
    print(type(retMes))
    return retMes


def gc_help():
    retMes = Embed(title=f"__**HELP DESK:**__", color=0x52FF00)
    empty = "᲼᲼᲼᲼᲼᲼᲼"
    commands = f"**{prefix}as**\n**{prefix}uas**\n**{prefix}help**\n**{prefix}print**\n**{prefix}removeall**"
    description = "*assign player to structure and spot*\n*un assign player or structure and spot*\n" \
                  "*view the helpdesk*\n*prints all the saved guild assignments*\n" \
                  "*removes all the saved guild assignments*"
    retMes.add_field(name="COMMANDS", value=commands, inline=True)
    retMes.add_field(name="᲼", value=empty, inline=True)
    retMes.add_field(name="DESCRIPTION", value=description, inline=True)
    return retMes