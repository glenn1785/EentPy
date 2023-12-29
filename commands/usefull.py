import discord
from discord.ext import commands
from config import *
import os
from defs.levels import *
import pyqrcode
from defs.weather import *
import requests
import datetime
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="quaker")


class usefull(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('usefull is ready')

    @commands.command()
    async def clear(self, ctx, x=1):
        if x <= clearlimit:
            deleted = await ctx.channel.purge(limit=int(x) + 1)
            print(deleted)
        else:
            await ctx.send('No Das teveel kut')

    @commands.command(aliases=['Level', 'lvl', 'Lvl'])
    async def level(self, ctx, member: discord.Member = False):
        users = db["Users"]

        if not member:
            id = ctx.message.author.id
            results = users.find({"_id": id})
            for result in results:
                exp = result['xp']
                lvl = result['level']
            await ctx.send(f'Ge zijt op level {lvl} en hebt {exp} xp!')
        else:
            id = member.id
            results = users.find({"_id": id})

            for result in results:
                    exp = result['xp']
                    lvl = result['level']
            await ctx.send(f'{member} heeft level {lvl} en heeft {exp} xp!')

            # if "pymongo.cursor.Cursor" in results:
            # await ctx.send("User not found!")

    @commands.command()
    async def report(self, ctx, *, bug):
        em = discord.Embed(title='Merci he!',description="We zullen is zien da we er iets mee zijn", color=discord.Color.red())
        em.add_field(name='U zaagsel:', value=bug)
        em.set_thumbnail(url=botlogo)
        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
        await ctx.send(embed=em)
        em.add_field(name='Reporter',value=ctx.author,inline=False)
        owner = await self.client.fetch_user('488733167776432128')
        channel = await owner.create_dm()
        await channel.send(embed=em)

    @report.error
    async def rep_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title='Waarover wilde zage das ook alty handig...', color=discord.Color.red())
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await ctx.send(embed=em)

    @commands.command(aliases=['Naam'])
    async def naam(self, ctx, member: discord.Member = False):
        if not member:
            await ctx.send(f'Uwe naam is {ctx.author}.')
        else:
            await ctx.send(f'Zijne naam is {member}')

    @commands.command()
    async def addxp(self, ctx, xp, user: discord.Member = False):
        if not user:
            await ctx.send('tis wel py addxp ``xp`` ``user`` he dkzk.')
        else:
            if ctx.author.id == 488733167776432128:
                users = db["Users"]
                await update_data(users, user,int(xp))
                await ctx.send(f'added {xp} xp to {user}')
                if await level_up(users, user):
                    results = users.find({"_id": user.id})
                    for result in results:
                        lvl_end = result['level']
                    await ctx.send(f'{user.mention} Is naar level {lvl_end} gegaan!')

    @addxp.error
    async def rep_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('tis wel -addxp ``xp`` ``user`` he dkzk.')

    @commands.command(aliases=['qr', 'Qr', 'Generateqr'])
    async def generateqr(self, ctx, *, tekst):
        url = pyqrcode.create(tekst)
        url.png('myqr.png', scale=6)
        with open('myqr.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
        os.remove('myqr.png')

    @commands.command(aliases=['Weer', 'weer', 'weerbericht', 'Frank', 'frank'])
    async def Weerbericht(self, ctx, Location):
        url = "https://api.tomorrow.io/v4/timelines"
        querystring = {
            "location": getcoordinates(Location),
            "fields": ["temperature", "cloudCover", "windSpeed", "weatherCode","visibility"],
            "units": "metric",
            "timesteps": "1h",
            "timezone": "Europe/Brussels",
            "apikey": tommorowiokey}

        response = requests.request("GET", url, params=querystring)

        results = response.json()['data']['timelines'][0]['intervals']
        now = datetime.datetime.now()
        curday = now.day
        em = discord.Embed(title=f'Weer per uur van vandaag in {geolocator.geocode(Location)}:',description='Bron: tomorrow.io',color=discord.Color.blue())
        for daily_result in results:
            hour = daily_result['startTime'][11:16]
            if int(daily_result['startTime'][8:10]) == int(curday):
                weatherCode = daily_result['values']["weatherCode"]
                weather = getweather(weatherCode)
                temp = round(daily_result['values']['temperature'])
                windspeed = daily_result['values']['windSpeed']
                visibility = daily_result['values']['visibility']
                em.add_field(name=f'{hour}:',value=f'**-Weer type: **{weather}\n**-Temp:** {temp}°C\n**-Windsnelheid:** {windspeed}m/s\n**-Zichtbaarheid:** {visibility}km')
        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
        em.set_thumbnail(url='https://i.postimg.cc/dt9Xg39D/frank-deboosere.jpg')
        await ctx.send(embed=em)

    @Weerbericht.error
    async def weater_err(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            em=discord.Embed(title='Geen locatie',description='K kan ni rieken waar gy zit!',color=discord.Color.red())
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await ctx.send(embed=em)

    @commands.command()
    async def emojiid(self, ctx, *, emojis):
        await ctx.send(f"magic:```{emojis}```")

    @commands.command()
    async def id(self, ctx, member: discord.Member=False):
        if not member:
            member = ctx.author
        await ctx.send(f"Den idee van **{member.display_name}** is: **{member.id}**")

    @commands.command()
    async def code(self, ctx, *, code):
        await ctx.send(f"Hier is uwen code (python), wa ge ook van plan zijt:\n```py\n{code}```")


async def setup(client):
    await client.add_cog(usefull(client))
