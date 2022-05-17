# *     |\__/,|   (`\
# *   _.|o o  |_   ) )
# * -(((---(((--------
# *
# * Made by : Corsolaa
# * Date    : 17/05/2022
# * * * * * * * * * * * *
import discord
from unAssign import gc_unassign
from discord.ext import commands
from helpdesk import gc_help
from assign import gc_assign
from prefix import prefix
from removeall import gc_removeall, gc_removealls
from print import gc_print
from emojiregister import gc_emojiregister

token = open("text_files/token.txt", "r").read()
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")
auto = False


@bot.command()
async def autoprint(ctx):
    global auto
    if auto is True:
        auto = False
        await ctx.send("autoprint false")
    elif auto is False:
        auto = True
        await ctx.send("autoprint true")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def uas(ctx, build=None, spot=None):
    retMes = gc_unassign(build, spot)
    if isinstance(retMes, discord.embeds.Embed):
        await ctx.send(embed=retMes)
    else:
        await ctx.send(retMes)
        if auto is True:
            await _print(ctx)


@bot.command(name="print")
async def _print(ctx):
    retMes = gc_print()
    if isinstance(retMes, list):
        channel = bot.get_channel(964572292417986680)
        await channel.purge()
        for x in retMes:
            await channel.send(x)
    else:
        await ctx.send(retMes)


@bot.command(name="as")
async def _as(ctx, build=None, spot: int = 1, user=None):
    if not user:
        user = f"<@{ctx.author.id}>"
    retMes = gc_assign(build, spot, user)
    if isinstance(retMes, discord.embeds.Embed):
        await ctx.send(embed=retMes)
    else:
        await ctx.send(retMes)
        if auto is True:
            await _print(ctx)


@bot.command(name="help")
async def _help(ctx):
    await ctx.send(embed=gc_help())


@bot.command()
async def rem(ctx):
    await ctx.send(gc_removeall())


@bot.command()
async def rems(ctx):
    await ctx.send(gc_removealls())


@bot.command()
async def purge(ctx):
    await ctx.channel.purge()


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.event
async def on_reaction_add(reaction, user):
    if not gc_emojiregister(reaction, user):
        await reaction.remove(user)


@bot.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    message.content = message.content.lower()
    await bot.process_commands(message)


bot.run(token)
