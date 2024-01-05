import discord
from discord.ext import commands
from discord.ext import tasks
import random
import config
from config import *
import asyncio
import re
from defs.levels import *
from defs.servers import *


class onmessage(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.Clearfile.start()
        print('on_message is ready')

    @commands.Cog.listener()
    async def on_message(self, message):
        users = config.db["Users"]
        servers = config.db["Servers"]

        if not isinstance(message.channel, discord.channel.DMChannel):
            serverid = False
            spamchannelid = False
            results = servers.find({"_id": message.guild.id})
            for result in results:
                spamchannelid = result['spamchannel']
                serverid = result['_id']

            if bannedWords is not None and (isinstance(message.channel, discord.channel.DMChannel) == False):
                for bannedWord in bannedWords:
                    if msg_contains_word(message.content.lower(), bannedWord):
                        await message.delete()
                        await message.channel.send(
                            f"{message.author.mention} kheb u bericht verwijderd want der stond een stout woord in. {mvrwLarivier}")

            if random.randint(1, 5) == 1:
                if 'cassé' in message.content.lower() and message.author != self.client.user:
                    if random.randint(1, 5) == 1:
                        await message.channel.send(f'{message.author.mention}  is  cassé.')
                    else:
                        await message.channel.send(f'{message.author.mention} wie of wa is er nu weer cassé?')

                elif 'ajeu' in message.content.lower() and message.author != self.client.user:
                    await message.channel.send(f'{message.author.mention} wa doet er nu weer zeer?')

                elif ' gr ' in message.content.lower() or 'grr' in message.content.lower() or 'grrr' in message.content.lower() and message.author != self.client.user:
                    await message.channel.send(f'{message.author.mention} ni boos worden plss :pleading_face:')

                elif 'rip' in message.content.lower() and message.author != self.client.user:
                    await message.channel.send(f'F in the chat for {message.author.mention}')
                    await message.channel.send('f')

                elif 'mhm' in message.content.lower() and message.author != self.client.user:
                    await message.channel.send(f'Mhmm where are you thinking about {message.author.mention}?')
            if message.content.lower() == "pls meme":
                await message.channel.send("ey dikzak ga is ni bij de concurtentie danku")

            if message.author != self.client.user and f'{message.guild.id}' in f'{serverid}' and f'{spamchannelid}' != f'{message.channel.id}':
                counter = 0
                with open("antispam.txt", "r+") as f:
                    for lines in f:
                        if lines.strip("\n") == str(message.author.id):
                            counter += 1

                    f.writelines(f"{str(message.author.id)}\n")
                    if counter > 5:
                        await message.channel.purge(limit=5)
                        await message.channel.send(f"ey {message.author.mention} stop me spammen")
                        if not message.author.bot:
                            channel = await message.author.create_dm()
                            await channel.send(
                                f"Ey {message.author.mention} stop is me spammen in {message.guild} AUB, danku")

            updateservers(servers, message.guild)

            if not message.author.bot:
                await update_data(users, message.author, 5)

                if await level_up(users, message.author):
                    results = users.find({"_id": message.author.id})
                    for result in results:
                        lvl_end = result['level']
                    await message.channel.send(f'{message.author.mention} is naar lvl {lvl_end} gegaan')

            if (
                    message.content == f"**EENTDMOMENT**{config.eent}" or message.content == f"**EENTDMOMENT**{config.eent} NEP") and str(
                message.author.id) == "988143343559127090":

                await message.add_reaction(config.eent)
                owner = await self.client.fetch_user('703596839093665832')
                channel = await owner.create_dm()

                async for msg in channel.history(limit=1):
                    if msg.author.id == self.client.user.id:
                        await msg.delete()

                await channel.send("<@!703596839093665832> there is a eentmoment")

            elif str(message.author.id) != "988143343559127090" and message.author.bot == False:
                # gaat weg
                for i in range(0, len(config.greets)):
                    if msg_contains_word(message.content.lower(), config.greets[i]):
                        await message.channel.send(
                            f"{config.greets[random.randint(0, len(greets) - 1)]} {message.author.display_name}")
                        break
                # komt aan
                for i in range(0, len(config.othergreets)):
                    if msg_contains_word(message.content.lower(), config.othergreets[i]):
                        await message.channel.send(
                            f"{config.othergreets[random.randint(0, len(config.othergreets) - 1)]} {message.author.display_name}")
                        break

    @tasks.loop(seconds=10)
    async def Clearfile(self):
        await asyncio.sleep(10)
        with open("antispam.txt", "r+") as f:
            f.truncate(0)


def msg_contains_word(msg, word):
    return re.search(fr'\b({word})\b', msg) is not None


async def setup(client):
    await client.add_cog(onmessage(client))
