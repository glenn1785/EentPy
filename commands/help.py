import discord
from discord.ext import commands

import config
from defs.levels import *


class help(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('help is ready')

    @commands.command(aliases=['Help','Hepl','hepl'])
    async def help(self, ctx, subCat = "False"):
        if subCat == "False":
            em = discord.Embed(title="Hier ziede wa ik allemaal kan:",  description="Voor meer info stuur \"py help [categorie]\"", color=discord.Color.yellow())
            em.add_field(name="Usefull:", value="```weerbericht \ngenerateqr \nemojiid \nreport \nclear \nlevel \ncode \nnaam \nid```")
            em.add_field(name="Fun:", value="```emojiflip \ncoinflip \n8ball \nslaag \nhack \nmeme \nping \nzeg```")
            em.add_field(name="Rekenen:", value="```calculate \nfactorial \nconvert \nrandom \npi```")
            em.add_field(name="Games:", value="```raadhetnummer \ntictactoe \nlogogame  \nf1game \nsoccer ```")
            em.add_field(name="Info:", value="```gebruikersinfo \nserverinfo \nstockinfo \nbotinfo```")
            em.add_field(name="Verjaardag:", value="```zetverjaardag \nverjaardag```")
            em.set_thumbnail(url=config.botlogo)
            em.set_footer(text='Powered by Eent.py', icon_url=config.botlogo)
            await ctx.send(embed=em)
        elif subCat.lower() == "verjaardag":
            await ctx.send("help verjaardag")
        elif subCat.lower() == "fun":
            await ctx.send("help fun")
        elif subCat.lower() == "games":
            await ctx.send("help games")
        elif subCat.lower() == "info":
            await ctx.send("help info")
        elif subCat.lower() == "rekenen":
            await ctx.send("help rekenen")
        elif subCat.lower() == "stock":
            await ctx.send("help stock")
        elif subCat.lower() == "handig":
            await ctx.send("help handig")
        else:
            await ctx.send("Da zal chezzi nog moeten uitvinden")


async def setup(client):
    await client.add_cog(help(client))
