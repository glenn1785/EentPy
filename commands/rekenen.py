import discord
from discord.ext import commands
from config import *

import random
import defs.calculate
from defs.binhexdec import *


import math

class Math(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('math is ready')

    def factorial(self, n):
        if n <= 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    @commands.command(aliases=["random"])
    async def Random(self, ctx, inpUt):

        minn = ""
        maxx = ""
        komma = False
        for i in range(0, len(inpUt)):
            if inpUt[i] != ',' and not komma:
                minn += inpUt[i]

            elif komma:
                maxx += inpUt[i]

            else:
                komma = True
        await ctx.send(f"Is dees random genoeg?: {random.randint(int(minn), int(maxx))}")

    @Random.error
    async def random_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('py random [minnumb],[maxnumb]')

    @commands.command(aliases=['calc', 'calculate'])
    async def Calculate(self, ctx, input):
        output = defs.calculate.calculate(input)
        embed = discord.Embed(title="berekenen", color=discord.Colour.dark_blue())
        embed.add_field(name="Gekke berekening", inline=False, value=f"```{input}```")
        embed.add_field(name="Antwoord op uwen gekke berekening", inline=False, value=f"```= {output}```")
        await ctx.send(embed=embed)

    @Calculate.error
    async def calculate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"alz hier is uwe syntax\n[calc, calculate] [berekening me + - * /]")

    @commands.command()
    async def pi(self, ctx):
        await ctx.send(embed=discord.Embed(title=f"pi = {float(math.pi)}", description="azubliev", colour=discord.Colour.blue()))

    @commands.command(aliases=["fact", "factorial"])
    async def Factorial(self, ctx, n):
        embed = discord.Embed(title="Factorial", color=discord.Colour.dark_blue())
        embed.add_field(name=f"De factorial van {n}", value=f'```={self.factorial(float(n))}```')
        await ctx.send(embed=embed)

    @Factorial.error
    async def fact_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("[fact/factorial] [number]")

    @commands.command(aliases=["conv"])
    async def convert(self, ctx, inputnumb):
        self.input = inputnumb

        if inputnumb[0] == "0":
            if inputnumb[1] == "x":
                Hex(self)
                firstcode = "hexadecimal"
            elif inputnumb[1] == 'b':
                try:
                    x = int(inputnumb[-2:])
                    Bin(self)
                    firstcode = "binary"
                except ValueError:
                    self.output1 = "PLEASE DON'T USE LETTERS FOR A BIN NUMBER" "please don't use letters for a bin number"
                    self.output2 = ""
                    firstcode = "an error"
        else:
            try:
                x = int(inputnumb)
                dec(self)
                firstcode = "decimal"
            except ValueError:
                self.output1 = "please don't use letters for a dec number"
                self.output2 = ""
                firstcode = "an error"

        em = discord.Embed(title=f"convert from {firstcode}", color=discord.Colour.green())

        await ctx.send(embed=em)

        await ctx.send(f"{self.output1}\n{self.output2}")

        await ctx.send("**DEES COMMAND WERKT NIET VOLLEDIG DUS REKENT NI OP DEES E (kben gwn te tam om da er ff uit te halen...)**")


async def setup(bot):
    await bot.add_cog(Math(bot))
