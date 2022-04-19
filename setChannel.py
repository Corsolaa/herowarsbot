# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 19/04/2022
# * * * * * * * * * * * *
# import os
# checkSend = os.stat("./text files/sendChannel.txt").st_size
# checkLand = os.stat("./text files/landChannel.txt").st_size
#
#
# def set_send(ctx):
#     retMes = "Send channel already set..."
#     if checkSend == 0:
#         file = open("./text files/sendChannel.txt", "a")
#         file.write(str(ctx.channel.id))
#         retMes = "You can now set assignments here..."
#     return retMes


# def set_land(ctx):
#     retMes = ""
#     if checkSend > 1:
#         retMes = "Landing channel already set..."
#         if checkLand == 0:
#             file = open("./text files/landChannel.txt", "a")
#             file.write(str(ctx.channel.id))
#             retMes = "You can now print the assignments out here...."
#     return retMes
