import discord
from discord.ext import commands
import time
import os
import config
import datetime
import json
from config import *
from defs.levels import *
import asyncio


class info(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('info is ready')

    @commands.command(aliases=['Gebruikersinfo', 'info', 'Info'])
    async def gebruikersinfo(self, ctx, member: discord.Member = False):
        msg = await ctx.send('Kzen is aant zien wa k weet he...')
        if not member:
            member = ctx.author 
        id = member.id 
        em = discord.Embed(title="Dees hem k gevonden :eyes:", color=discord.Color.blue())
        async with ctx.typing():
            await asyncio.sleep(1)

        users = config.db["Users"]

        results = users.find({"_id": id})

        for result in results:
            exp = result['xp']
            lvl = result['level']

        em.add_field(name='Gebruikersnaam:', value=member)
        em.add_field(name="Server naam:", value=member.display_name)
        em.add_field(name='Id:', value=member.id)
        em.add_field(name='Level:', value=lvl)
        em.add_field(name='XP:', value=exp)
        em.add_field(name='Status:', value=member.status, inline=True)
        em.add_field(name='In de kelder beland op:', value=member.joined_at.strftime("%a, %d %b %Y, %H:%M  %Z"))
        em.add_field(name='Dees acc is geboren op:', value=member.created_at.strftime("%a, %d %b %Y, %H:%M  %Z"))
        em.set_thumbnail(url=member.avatar)
        em.set_footer(text=f"Gevraagd door {ctx.author}")
        await msg.edit(embed=em)

    @commands.command(aliases=['Serverinfo', 'Server', 'server'])
    async def serverinfo(self, ctx):
        async with ctx.typing():
            await asyncio.sleep(0.5)
        guild = ctx.guild
        em = discord.Embed(title="Een beeke info over deze zever:", description=guild.description,
        color=discord.Color.blue())
        em.add_field(name='Den big boss:', value=guild.owner)
        em.add_field(name='Server id:', value=guild.id)
        em.add_field(name='T aantal idoiten:', value=guild.member_count)
        em.add_field(name='Gebouwd op:', value=ctx.guild.created_at.strftime("%a, %d %b %Y, %H:%M  %Z"))
        em.set_footer(text=f"Gevraagd door {ctx.author}")
        em.set_thumbnail(url=ctx.guild.icon)
        await ctx.send(embed=em)



    @commands.command(aliases=['bot','Bot','Botinfo'])
    async def botinfo(self,ctx):
        member = await self.client.fetch_user(config.bot_id)
        now = datetime.datetime.utcnow()
        elapsed = now - starttime
        seconds = elapsed.seconds
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        em = discord.Embed(title="Eent.py's info:", description=f'momentele versie: {config.bot_version}',
                           color=discord.Color.blue())
        em.add_field(name='Gebruikersnaam:', value=member)
        em.add_field(name="Servernaam:", value=member.display_name)
        em.add_field(name='Gebruikers idee:', value=member.id)
        em.add_field(name='Status:', value='Online', inline=True)
        em.add_field(name='Hoe lang da k al werk zonder slaap :sleeping: :', value=f'{elapsed.days}d {hours}h {minutes}m {seconds}s')
        em.add_field(name='Made in:',value='Replit')
        #em.add_field(name='In dienst genomen:', value=member.joined_at.strftime("%a, %d %b %Y, %H:%M  %Z"))
        em.add_field(name='Bot gefabriceerd:', value=member.created_at.strftime("%a, %d %b %Y, %H:%M  %Z"))
        em.add_field(name='Mijnen Website:', value='https://Eentpy.pepijnsimoens.repl.co')
        em.set_thumbnail(url=config.botlogo)
        em.set_footer(text='Powered by Eent.py', icon_url=config.botlogo)
        await ctx.send(embed=em)



starttime = datetime.datetime.utcnow()


async def setup(client):
    await client.add_cog(info(client))
