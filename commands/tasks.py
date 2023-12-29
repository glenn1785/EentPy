import discord
from discord.ext import commands
import random
import time
import datetime
import config
from config import *
from discord.ext import tasks
from defs.levels import *
from defs.weather import *
import requests
from defs.botLogboek import addEvent
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="eentpy")


class tasks(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.gmgn.start()
        print('tasks is ready')



    @tasks.loop(hours=1)
    async def gmgn(self):
        global db
        now = datetime.datetime.now()
        curmonth = now.month
        curday = now.day
        curyear = now.year
        users = db["Users"]

        if int(time.strftime("%H")) == 6:
            url = "https://api.tomorrow.io/v4/timelines"
            querystring = {
                            "location": getcoordinates("Merchtem"),
                            "fields": ["temperature", "cloudCover", "windSpeed", "weatherCode","moonPhase"],
                            "units": "metric",
                            "timesteps": "1d",
                            "timezone": "Europe/Brussels",
                            "apikey": tommorowiokey}
            
            response = requests.request("GET", url, params=querystring)
            results = response.json()['data']['timelines'][0]['intervals']
            todayweather = '\u200b'
            for daily_result in results:
                date = daily_result['startTime'][0:10]
                hour = daily_result['startTime'][11:16]
                if int(daily_result['startTime'][8:10]) == int(curday):
                    weatherCode = daily_result['values']["weatherCode"]
                    weather = getweather(weatherCode)
                    phasecode = daily_result['values']["moonPhase"]
                    moonphase = getmoonphase(phasecode)
                    temp = round(daily_result['values']['temperature'])
                    todayweather = f'Frank zegt da t {weather} gaat zijn en {temp}°C.\n**Maan fase:**\n{moonphase}'
            

            em = discord.Embed(title=f'Goeiemorgen kindjesss!!', color=discord.Color.blue())
            em.add_field(name='Tijd om op te staan!', value='Nu aant werk!',inline=False)
            em.add_field(name=':date: Den datum want we zijn hier te skeer voor ne scheurkalender:', value=f'{curday}/{curmonth}/{curyear}',inline=False)
            em.add_field(name=':1234: Random nummer van de dag:', value=random.randint(1, 200), inline=False)
            em.add_field(name=f':white_sun_small_cloud: Weer of geen weer ge moet werken:', value=todayweather, inline=False)
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            em.set_thumbnail(url=config.botlogo)

            results = users.find({"b-day": f'{curday}',"b-month": f'{curmonth}'})
            for result in results:
                year = int(result['b-year'])
                userid = result['_id']
                mname = await self.client.fetch_user(userid)
                em.add_field(name=f':tada: Gelukkige verjaadag: weer een jaartje dichter bij de dood', value=f'{mname.mention} ({curyear-year})', inline=False)

            channel = self.client.get_channel(int("828977083484864522"))
            await channel.send(embed=em)
                
            #servers.update_one({"_id": guildid}, {"$set": {"lastgm": f'{curday}'}}) 

        if int(time.strftime("%H")) == 20:
            em = discord.Embed(title=f'Tijd om te gaan pitten', color=discord.Color.blue())
            em.add_field(name=f'Oogjes toe en snaveltjes dicht!!',
                         value=f"Mnr Sarens bewaakt de weerstanden wel {Mnrsarens}")
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            em.set_image(url='https://i.postimg.cc/PxV0hhY2/gn.png')
            channel = self.client.get_channel(int("828977083484864522"))
            await channel.send(embed=em)
            #servers.update_one({"_id": guildid}, {"$set": {"lastgn": f'{curday}'}})


async def setup(client):
    await client.add_cog(tasks(client))