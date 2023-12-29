import discord
from discord.ext import commands
import random
import time
from config import *
import asyncio
from defs.levels import *
from discord.ext import tasks
from defs.botLogboek import addEvent
beurt = 1
firstuser = False
seconduser = False
caller = False


class eentmoment(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.eentmoment.start()
        print('eentmoment is ready')

    @tasks.loop(hours=1)
    async def eentmoment(self):
        if int(time.strftime("%H")) >= 6 and int(time.strftime("%H")) < 20:
            minutes = random.randint(10, 50) * 60
            await asyncio.sleep(minutes)
            channel = self.client.get_channel(828977083484864522)
            if int(time.strftime("%H")) == 10:
                Message = await channel.send(f"**EETMOMENT**{eent}")
            else:
                Message = await channel.send(f"**EENTMOMENT**{eent}")
            await Message.add_reaction("<:eentd:841755160531304480>")
            global beurt
            global messagesend
            collection = db["Bot-logboek"]
            addEvent(collection, "Eentmoment")
            messagesend = False
            beurt = 3

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        global beurt
        global firstuser
        global seconduser
        global messagesend
        users = db['Users']

        reactions = "<:eent:841755160531304480>"
        channel = self.client.get_channel(828977083484864522)
        if str(reactions) == str(reaction) and beurt == 3 and user.bot == False:

            await update_data(users, user, 100)

            if await level_up(users, user):
                results = users.find({"_id": user.id})
                for result in results:
                    lvl_end = result['level']
                await channel.send(f'{user.mention} is naar lvl {lvl_end} gegaan')

            if random.randint(1, 10) == 5:
                await channel.send(f'{user.mention} was eerst gy krijgt 100 XD! {eent}')
            else:
                await channel.send(f'{user.mention} was eerst gy krijgt 100 XP! {eent}')
            firstuser = user.id
            beurt = 2

        elif str(reactions) == str(reaction) and beurt == 2 and user.bot == False and user.id != firstuser:

            await update_data(users, user, 50)

            if await level_up(users, user):
                results = users.find({"_id": user.id})
                for result in results:
                    lvl_end = result['level']
                await channel.send(f'{user.mention} is naar lvl {lvl_end} gegaan')

            if random.randint(1, 10) == 5:
                await channel.send(f'{user.mention} was tweede gy krijgt 50 XD! {eent}')
            else:
                await channel.send(f'{user.mention} was tweede gy krijgt 50 XP! {eent}')
            seconduser = user.id
            beurt = 1

        elif str(reactions) == str(reaction) and beurt == 1 and user.bot == False and user.id != firstuser and user.id != seconduser:
            await channel.send(f'{user.mention} gy waart te traag sukkel niks voor u {eent}')
            beurt = False

    @commands.command(aliases=['Eentd'])
    async def eent(self, ctx):
        if random.randint(1, 30) == 25:
            em = discord.Embed(title=f"**EENTMOMENT**{eent}")
            em.set_image(
                url='https://tenor.com/view/rickroll-lyrics-80s-never-gonna-give-you-up-rick-astley-gif-21869209')
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await ctx.send(embed=em)
        else:
            Message = await ctx.send(f"**EENTMOMENT**{eent}")
            await Message.add_reaction("<:eent:841755160531304480>")


async def setup(client):
    await client.add_cog(eentmoment(client))
