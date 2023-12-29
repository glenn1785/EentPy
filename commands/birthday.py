import discord
from discord.ext import commands
from config import *
import os
from defs.birthday import *


class birthdays(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('birthdays is ready')

    @commands.command(aliases=['Zetverjaardag'])
    async def zetverjaardag(self,ctx):
        member = ctx.author
        users = db['Users']

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        results = users.find({"_id": member.id})
        for result in results:
            day = result['b-day']
            month = result['b-month']
            year = result['b-year']
            if day != 'NaN':
                await ctx.send(f'Kweet al da gy geboren zijt op {day}/{month}/{year}!\n'
                               f'Zijde ineens op nen andere dag geboren ``y/n``!')
                msg = await self.client.wait_for('message', check=check)
                if msg.content.lower() == 'y':
                    await ctx.send('Zegt t nog is opnieuw dan gebruik wel t DD/MM/JJJJ formaat.')
                    msg = await self.client.wait_for('message', check=check)
                    list = msg.content.split("/")
                    try:
                        day = int(list[0])
                        month = int(list[1])
                        year = int(list[2])
                    except ValueError:
                        await ctx.send(f'Die dag is {nibien}')
                    valid_day = await check_day(month, day)
                    if valid_day:
                        await update_birthday(users, member, day, month, year)
                        await ctx.send(f'Allz tis gelukt nu zijde geboren op {day}/{month}/{year}!')
                    else:
                        await ctx.send(f'Die dag is {nibien}')
                    return
                else:
                    await ctx.send('K stop ermee...')
                    return

            else:
                await ctx.send("Wnr zijde geboren? Gebruik DD/MM/JJJJ formaat merci.")

                msg = await self.client.wait_for('message', check=check)

                list = msg.content.split("/")
                try:
                    day = int(list[0])
                    month = int(list[1])
                    year = int(list[2])
                except ValueError:
                    await ctx.send(f'Die dag is {nibien}')
                    return

                valid_day = await check_day(month, day)

                if valid_day:
                    await update_birthday(users, member, day, month, year)
                    await ctx.send(f'Allz tis gelukt nu zijde geboren op {day}/{month}/{year}!')
                else:
                    await ctx.send(f'Die dag is {nibien}')

    @commands.command(aliases=["Verjaardag"])
    async def verjaardag(self,ctx, user: discord.Member = False):
        users = db["Users"]

        if not user:
            user = ctx.author
            salution = "Uwen"
        else:
            salution = "Zijnnen"

        results = users.find({"_id": user.id})
        for result in results:
            day = result['b-day']
            month = result['b-month']
            year = result['b-year']
            if day == 'NaN':
                if salution == "Zijnnen":
                    await ctx.send(f"Kweet toch ni wnr die geboren is\n"
                                    "Vraag t hem is")
                else:
                    await ctx.send(f"Ge moet eerst wel zeggen wnr da gy geboren zijt he k kan da ni rieken"
                                   "Typt py zetverjaardag ")

            else:
                await ctx.send(f'{salution} geboortedatum is op {day}/{month}/{year}')


async def setup(client):
    await client.add_cog(birthdays(client))
  