# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 17/05/2022
# * * * * * * * * * * * *
from discord import Embed
from structures import structures
from prefix import prefix


def gc_allassign_help(title, color):
    retMes = Embed(title=f"__**{prefix}{title.upper()} HELPDESK:**__",
                   description=prefix + title + " {structs} {spot} {playername}", color=color)
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
    return retMes


def gc_help():
    retMes = Embed(title=f"__**HELPDESK:**__", color=0x52FF00)
    empty = "᲼᲼᲼᲼᲼᲼᲼"
    commands = f"**{prefix}as**\n**{prefix}uas**\n**{prefix}help**\n**{prefix}print**\n**{prefix}purge**\n" \
               f"**{prefix}rem**\n**{prefix}rems**\n**{prefix}ping**"
    description = "*assign player to structure and spot*\n*un assign player or structure and spot*\n" \
                  "*view the helpdesk*\n*prints all the saved guild assignments*\n*removes all messages in channel*\n" \
                  "*removes all the saved guild assignments*\n*removes all the saved emoji reactions on print*\n" \
                  "*pong*"
    retMes.add_field(name="COMMANDS", value=commands, inline=True)
    retMes.add_field(name="᲼", value=empty, inline=True)
    retMes.add_field(name="DESCRIPTION", value=description, inline=True)
    return retMes
