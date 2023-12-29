import os
import datetime
import time

import discord
from discord.ext import commands
from config import *
import asyncio
import pymongo
from keep_alive import keep_alive
#from defs.botLogboek import addEvent

# ToDo:
#  alle dinges aanpasse naar AV
#  eentmoment en lvl commands
#  allow en daag
#  useful commands (id, channelid, serverid, infodinges)
#  minigames

intents = discord.Intents.all()
client = commands.Bot(command_prefix=['py ', 'py', 'Py ', 'Py'], intents=intents)


client.remove_command("help")


@client.event
async def on_ready():
    # await load_extensions()
    await client.change_presence(activity=discord.Game(name=" me u dikke ma op een driewieler of nie dan?"))
    keep_alive()
    print(f'Bot is ready ({bot_version})')


# if a command does not exist
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(title="da kan deze domme computer ni ze",
                           description=f"haal miss {Mnrchezzi} of ni... {mvrwtroch}", color=discord.Color.red())
        em.add_field(name="wa ik kan?", value="vraag is aan <@!988143343559127090>")
        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
        em.set_thumbnail(url=botlogo)
        await ctx.send(embed=em)


@client.command()
async def version(ctx):
    await ctx.send(f"Mijne versie: {bot_version}")


@client.command()
async def time(ctx):
    await ctx.send(datetime.datetime.now())


# ---------------------- cogs ----------------

async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await client.load_extension(f"commands.{filename[:-3]}")


async def main():
    async with client:
        await load_extensions()
        await client.start(token)


asyncio.run(main())