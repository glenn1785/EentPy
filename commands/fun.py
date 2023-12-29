import discord
from discord.ext import commands
import random
import time
import asyncio
import config
from config import *
from lijsten.jokes import *
import praw




class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('fun is ready')

    @commands.command(aliases=['Ping'])
    async def ping(self, ctx):
        await ctx.send(f'**KWAK** {round(self.client.latency * 1000)}ms {eent}')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['Ja.',
                     'Waarschijnlijk.',
                     'wie weet',
                     'Kwni jong.',
                     'waarschijnlijk ni...',
                     'Kan zijn...',
                     'laat mij is denken...',
                     'OFCC!!!',
                     'Moet ge is aan ZALM vragen.']
        em = discord.Embed(title="8ball :8ball:", color=discord.Color.blue())
        em.add_field(name="U domme vraag:", value=question)
        em.add_field(name="Mijn super waar antwoord:", value=random.choice(responses), inline=False)
        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
        await ctx.send(embed=em)

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Stel een vraag jongeuh')

    @commands.command(aliases=['Zeg'])
    async def zeg(self, ctx, *, tekst):
        await ctx.message.delete()
        await ctx.send(tekst)

    @zeg.error
    async def zeg_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Wa moe k zeggen dan')

    @commands.command(aliases=['Hack'])
    async def hack(self, ctx, *, hack):
        ipaddress = ['192.451.515', '192.122.754', '192.784.734', '192.121.748']
        Username = ['123', '213', '456', '321']
        ctx = await ctx.send(f'hacking {hack}...')
        time.sleep(2)
        await ctx.edit(content='Finding IP-address...')
        time.sleep(2)
        await ctx.edit(content=f'IP-address is {random.choice(ipaddress)}')
        time.sleep(2)
        await ctx.edit(content=f'Finding Minecraft-username...')
        time.sleep(2)
        await ctx.edit(content=f'Minecraft-username is {hack}{random.choice(Username)}')
        time.sleep(2)
        await ctx.edit(content=f'Kzen klaar me de zeer gevaarlijke hack van {hack}!')

    @hack.error
    async def hack_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Wie moe k nu weer is hacken')

    @commands.command(aliases=['Slaag','klets','Klets','Kletz','kletz'])
    async def slaag(self, ctx, member: discord.User = None):
        gif = ['https://media1.tenor.com/images/bc858e69d5022807b84554b2d4583c10/tenor.gif?itemid=5013065',
               'https://media1.tenor.com/images/3c161bd7d6c6fba17bb3e5c5ecc8493e/tenor.gif?itemid=5196956',
               'https://media1.tenor.com/images/b3afc2339d254fea655bce6ccba73b2a/tenor.gif?itemid=15667197',
               'https://media1.tenor.com/images/49de17c6f21172b3abfaf5972fddf6d6/tenor.gif?itemid=10206784',
               'https://media1.tenor.com/images/0720ffb69ab479d3a00f2d4ac7e0510c/tenor.gif?itemid=10422113',
               'https://media1.tenor.com/images/8f437ee9e36b337149023dca87b97b07/tenor.gif?itemid=17283089',
               'https://media1.tenor.com/images/4ec47d7b87a9ce093642fc8a3c2969e7/tenor.gif?itemid=12667518']
        if (member == ctx.message.author or member == None):
            em = discord.Embed(title=f'{ctx.message.author.display_name} slaagt zijn eige lol...', color=discord.Color.red())
            em.set_footer(text=f'Mnr Sarens trekt 5 punten af van {ctx.author.display_name}!',
                          icon_url=FotoSarens)
            em.set_image(url=random.choice(gif))
            await ctx.send(embed=em)
        else:
            em = discord.Embed(title=f'{ctx.message.author.display_name} slaagt {member.display_name} in de face.',
                               color=discord.Color.red())
            em.set_footer(text=f'Mnr Sarens trekt 5 punten af van {ctx.author.display_name}!',
                          icon_url=FotoSarens)
            em.set_image(url=random.choice(gif))
            await ctx.send(embed=em)

    @slaag.error
    async def slaag_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Wie moet zarenzzzzz zlagen??? {zarenz}')

    @commands.command()
    async def coinflip(self, ctx):
        ctx = await ctx.send(f'Flipping the coin...')
        time.sleep(2)
        head = ['oint', 'ducc']
        Coin = random.choice(head)
        await ctx.edit(content=f'**{Coin}** lag vanboven')

    @commands.command()
    async def emojiflip(self, ctx):

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        emojis = [config.eent, config.Mnrsarens, config.nibien, config.onsnancy, config.mnrzonderbroeck,
                  config.mnrpeirsman, config.mvrwLarivier, config.zarenz, config.Mnrchezzi, config.mvrwtroch]
        emojistring = ""
        initem = discord.Embed(title="Emoji flip")
        for i in range(len(emojis)):
            emojistring = f"{emojistring} \n{i+1} : {emojis[i]}"

        initem.add_field(name="Typ start en k kies een random emoji:", value=emojistring)
        initem.set_footer(text='Powered by Eent.py', icon_url=botlogo)
        initmsg = await ctx.send(embed=initem)

        try:
            msg = await self.client.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send("Te traag sukkel doe opnieuw!")

        if msg.content.lower == "start":
            rollem = discord.Embed(title="emojiflip")
            rollem.add_field(name=random.choice(emojis), value="\u200b")
            rollem.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await initmsg.edit(embed=rollem)

    @commands.command(pass_context=True, aliases=['Meme'])
    async def meme(self, ctx):
        x = ['Is kijken...', 'geef mij een moment...', 'Is zoeken he...']
        await ctx.send(random.choice(x))
        titles = ['Een cool memeke voor u', 'Vers van de pers!', 'Speciaal voor u mijn schatteke']
        title = random.choice(titles)

        reddit = praw.Reddit(client_id='s5CYuoPjds3fIQ',
                             client_secret='UmjQOE4rUArFSzv40bdPOcRcPuSmTQ',
                             user_agent='Overall_Town1082')

        memes_submissions = reddit.subreddit('meme').hot()
        post_to_pick = random.randint(1, 25)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        embed = discord.Embed(title=title, description=submission.title, color=discord.Color.dark_blue())
        embed.set_footer(text='Powered by reddit', icon_url='https://i.postimg.cc/DZp2hBfv/reddit.png')
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)



"""
    @commands.command(aliases=['Joke'])
    async def joke(self,ctx):
        joke = random.choice(jokes)
        await ctx.send(joke)
"""


async def setup(client):
    await client.add_cog(fun(client))