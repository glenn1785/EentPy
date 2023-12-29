import discord
from discord.ext import commands
import random
from config import *
import asyncio
import json
import numpy as np

class games(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('games is ready')

    @commands.command(aliases=['Raadhetnummer', 'raadnr', 'Raadnr'])
    async def raadhetnummer(self, ctx):

        em = discord.Embed(title=f'{ctx.author.display_name} raad t nummer tussen 1 en 10...', description="Aja ge hebt 3 kansen anders :skull_crossbones: ",
                           color=discord.Color.blue())
        em.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/821800168957280317/844463015318257664/downloads.png')
        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
        await ctx.send(embed=em)

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        secretnumber = random.randint(1, 10)
        limit = 3
        end = False
        found = False
        tooslow = False

        for i in range(limit):
            try:
                msg = await self.client.wait_for('message', check=check, timeout=30)
            except asyncio.TimeoutError:
                em = discord.Embed(title=f'Te traag {ctx.author.display_name} :blue_car: !', description=f'Doe nog is opnieuw',
                                   color=discord.Color.red())
                em.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/821800168957280317/844463015318257664/downloads.png')
                em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                await ctx.send(embed=em)
                tooslow = True
                break

            guessnumber = msg.content
            try:
                if int(guessnumber) == int(secretnumber):
                    em = discord.Embed(title=f'Goe zo {ctx.author.display_name} {mvrwMaetenZZ}!',
                                       description='Ge kunt nog alty opnieuw doen', color=discord.Color.green())
                    em.set_thumbnail(
                        url='https://cdn.discordapp.com/attachments/821800168957280317/844463015318257664/downloads.png')
                    em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                    await ctx.send(embed=em)
                    end = True
                    found = True

                elif int(guessnumber) < int(secretnumber):
                    limit -= 1
                    if limit != 0:
                        em = discord.Embed(title=f'Te laag {ctx.author.display_name}, doe opnieuw',
                                           description=f' nog {limit} kansen.', color=discord.Color.red())
                        em.set_thumbnail(
                            url='https://cdn.discordapp.com/attachments/821800168957280317/844463015318257664/downloads.png')
                        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                        await ctx.send(embed=em)

                elif int(guessnumber) > int(secretnumber):
                    limit -= 1
                    if limit != 0:
                        em = discord.Embed(title=f'Te hoog  {ctx.author.display_name}, doe opnieuw',
                                           description=f' nog {limit} kansen.', color=discord.Color.red())
                        em.set_thumbnail(
                            url='https://cdn.discordapp.com/attachments/821800168957280317/844463015318257664/downloads.png')
                        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                        await ctx.send(embed=em)

                if end:
                    break

            except ValueError:
                limit -= 1
                em = discord.Embed(title=f'Wel een nummer ingeven he {ctx.author.display_name}, allz doe opnieuw',
                                   description=f' nog {limit} kansen.', color=discord.Color.red())
                em.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/821800168957280317/844463015318257664/downloads.png')
                em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                await ctx.send(embed=em)

        if not found and not tooslow:
            em = discord.Embed(title=f'GAME OVER {ctx.author.display_name}! :skull_crossbones: ', description=f'doe opnieuw as ge durft',
                               color=discord.Color.red())
            em.add_field(name=f'Het nummer was:', value=secretnumber)
            em.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/821800168957280317/844463015318257664/downloads.png')
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await ctx.send(embed=em)

    @commands.command(aliases=['Logogame', 'Logo', 'logo'])
    async def logogame(self, ctx):

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        with open('./lijsten/logogame.json', 'r') as f:
            logos = json.load(f)

        i = random.randint(0, 71)
        logo = logos[f'{i}']["name"]
        logolink = logos[f'{i}']["link"]

        em = discord.Embed(title='Logo quiz!',
                           description='Van welk merk is dees logo\nge hebt 20 seconde om te antwoorden!',
                           color=discord.Color.blue())
        em.set_image(url=logolink)
        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
        await ctx.send(embed=em)

        try:
            answer = await self.client.wait_for('message', check=check, timeout=20)

            if answer.content.lower() == logo.lower():
                em = discord.Embed(title=f'goe zo {ctx.author.display_name} {mvrwMaetenZZ}!', description='Type -logogame om opnieuw te spelen!',
                                   color=discord.Color.green())
                em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                await ctx.send(embed=em)

            else:
                em = discord.Embed(title=f'ni bien {ctx.author.display_name} {nibien}!', description=f'Type -logogame om opnieuw te spelen!',
                                   color=discord.Color.red())
                em.add_field(name='t just antwoord is:', value=logo)
                em.set_image(url=logolink)
                em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                await ctx.send(embed=em)

        except asyncio.TimeoutError:
            em = discord.Embed(title=f'traageeuuuuhhh{ctx.author.display_name} :blue_car:!', description=f'Type -logogame om opnieuw te spelen!',
                               color=discord.Color.red())
            em.add_field(name='t just antwoord is:', value=logo)
            em.set_image(url=logolink)
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await ctx.send(embed=em)
        with open('./lijsten/logogame.json', 'w') as f:
            json.dump(logos, f)

    @commands.command(aliases=['F1game', 'F1', 'f1'])
    async def f1game(self, ctx):

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        if random.randint(1, 2) == 1:
            with open('./lijsten/f1_logogame.json', 'r') as f:
                logos = json.load(f)
            i = random.randint(1,10)

            logo = logos[f'{i}']["name"]
            logolink = logos[f'{i}']["link"]

            em = discord.Embed(title='Logo quiz f1 super deluxe premium editie!',
                               description='van wa team is deze foto?\nge hebt  20 seconden om tantwoorde!',
                               color=discord.Color.blue())
            em.set_image(url=logolink)
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await ctx.send(embed=em)

            try:
                answer = await self.client.wait_for('message', check=check, timeout=20)

                if answer.content.lower() == logo.lower():
                    em = discord.Embed(title=f'Goe zo {ctx.author.display_name} {mvrwMaetenZZ}!', description='Type py F1game om nog nekeer te spele!',
                                       color=discord.Color.green())
                    em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                    await ctx.send(embed=em)

                else:
                    em = discord.Embed(title=f'Ni bien {ctx.author.display_name} {nibien}!', description=f'Type py F1game om nog nekeer te spele!',
                                       color=discord.Color.red())
                    em.add_field(name='t juste antwoord:', value=logo)
                    em.set_image(url=logolink)
                    em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                    await ctx.send(embed=em)

            except asyncio.TimeoutError:
                em = discord.Embed(title=f'Te traag {ctx.author} :blue_car: !', description=f'Type py F1game om nog nekeer te spele!',
                                   color=discord.Color.red())
                em.add_field(name='t juste antwoord:', value=logo)
                em.set_image(url=logolink)
                em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                await ctx.send(embed=em)
            with open('./lijsten/f1_logogame.json', 'w') as f:
                json.dump(logos, f)

        else:
            with open('./lijsten/f1_trackgame.json', 'r') as f:
                tracks = json.load(f)
            i = random.randint(0, 26)
            track = tracks[f'{i}']["name"]
            tracklink = tracks[f'{i}']["link"]

            em = discord.Embed(title='F1 track quiz!',
                               description='hoe noemt dees?\n20 sec om te antwoorden!!',
                               color=discord.Color.blue())
            em.set_image(url=tracklink)
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await ctx.send(embed=em)

            try:
                answer = await self.client.wait_for('message', check=check, timeout=20)

                if answer.content.lower() == track.lower():
                    em = discord.Embed(title=f'goe zo {ctx.author} {mvrwMaetenZZ}!', description='Type py F1game om nog nekeer te spele!',
                                       color=discord.Color.green())
                    em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                    await ctx.send(embed=em)

                else:
                    em = discord.Embed(title=f'ni goe {ctx.author.display_name} {nibien}!', description=f'Type py F1game om nog nekeer te spele!',
                                       color=discord.Color.red())
                    em.add_field(name='t juste antwoord:', value=track)
                    em.set_image(url=tracklink)
                    em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                    await ctx.send(embed=em)

            except asyncio.TimeoutError:
                em = discord.Embed(title=f'trageuhhh {ctx.author} :blue_car:!', description=f'Type -F1game om nog nekeer te spele!',
                                   color=discord.Color.red())
                em.add_field(name='t juste antwoord:', value=track)
                em.set_image(url=tracklink)
                em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                await ctx.send(embed=em)
            with open('./lijsten/f1_trackgame.json', 'w') as f:
                json.dump(tracks, f)

    @commands.command()
    async def f1test(self,ctx):
        with open('./lijsten/f1_trackgame.json', 'r') as f:
            tracks = json.load(f)
        for track in tracks:
            em=discord.Embed(title=tracks[f'{track}']['name'])
            em.set_image(url=tracks[f'{track}']['link'])
            message = await ctx.send(embed=em)
            await message.add_reaction("❌")
            await message.add_reaction("✅")
            await asyncio.sleep(2)
        with open('./lijsten/f1_trackgame.json', 'w') as f:
            json.dump(tracks, f)


    @commands.command(aliases=['Soccer'])
    async def soccer(self, ctx):

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        em = discord.Embed(title='trapt die bal in de goal, liefst ni in de keeper zijn smoel.',
                           description='typt **`links`, `rechts` or `midden`**.', color=discord.Color.blue())

        places = ['links', 'midden', 'rechts']
        place = random.choice(places)
        if place == 'links':
            em.add_field(name=f':goal: :goal: :goal:\n:person_standing:', value='\u200b')
        if place == 'rechts':
            em.add_field(name=f':goal: :goal: :goal:\n              :person_standing:', value='\u200b')
        if place == 'midden':
            em.add_field(name=f':goal: :goal: :goal:\n       :person_standing:', value='\u200b')
        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
        msgb = await ctx.send(embed=em)

        for i in range(100):
            try:
                msg = await self.client.wait_for('message', check=check, timeout=2)
                if msg.content.lower() in places:
                    if msg.content.lower() == place:
                        em = discord.Embed(
                            title=f'Ni vandaag {mnrzonderbroeck}',
                            description='typt py soccer om opnieuw te proberen', color=discord.Color.red())
                        if place == 'links':
                            em.add_field(name=f':goal: :goal: :goal:\n:person_standing:',
                                         value=f'Your target: {msg.content.lower()}')
                        if place == 'rechts':
                            em.add_field(name=f':goal: :goal: :goal:\n              :person_standing:',
                                         value=f'Your target: {msg.content.lower()}')
                        if place == 'midden':
                            em.add_field(name=f':goal: :goal: :goal:\n       :person_standing:',
                                         value=f'U doel...: {msg.content.lower()}')
                        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                        await ctx.send(embed=em)
                        break

                    else:
                        em = discord.Embed(
                            title=f'Goe zo 5/10 {mnrzonderbroeck}',
                            description='typt py soccer om opnieuw te proberen', color=discord.Color.green())
                        if place == 'links':
                            em.add_field(name=f':goal: :goal: :goal:\n:person_standing:', value='\u200b')
                        if place == 'rechts':
                            em.add_field(name=f':goal: :goal: :goal:\n              :person_standing:', value='\u200b')
                        if place == 'midden':
                            em.add_field(name=f':goal: :goal: :goal:\n       :person_standing:', value='\u200b')
                        em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                        await ctx.send(embed=em)
                        break

                else:
                    await ctx.send(f"Broer da was er helemaal naast op {onsnancy} nog een verstrooidheid erbij, ge moet genen bananebal doen e")


            except asyncio.TimeoutError:
                em = discord.Embed(title='trapt die bal in de goal, liefst ni in de keeper zijn smoel.',
                                   description='type **`links`, `rechts` or `midden`**.', color=discord.Color.blue())

                place = random.choice(places)
                if place == 'links':
                    em.add_field(name=f':goal: :goal: :goal:\n:person_standing:', value='\u200b')
                if place == 'rechts':
                    em.add_field(name=f':goal: :goal: :goal:\n              :person_standing:', value='\u200b')
                if place == 'midden':
                    em.add_field(name=f':goal: :goal: :goal:\n       :person_standing:', value='\u200b')
                em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                await msgb.edit(embed=em)

    @commands.command(aliases=['Tictactoe'])
    async def tictactoe(self,ctx, member: discord.Member = False):
        if not member:
            await ctx.send('No friends mode geactiveerd, mentiont een vriend de volgende keer (als ge da hebt)')
            member = ctx.author

        def checkx(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        def checko(msg):
            return msg.author == member and msg.channel == ctx.channel
        turn = 'X'
        count = 0

        board = {"7": ':seven:', "8": ':eight:', "9": ':nine:',
                 "4": ':four:', "5": ':five:', "6": ':six:',
                 "1": ':one:', "2": ':two:', "3": ':three:'}
        board_keys = []

        places = ['1','2','3','4','5','6','7','8','9']

        for key in board:
            board_keys.append(key)
        em = discord.Embed(title=f'TicTacToe: {ctx.author} (X) VS {member} (O).', color=discord.Color.blue())
        em.add_field(name=f"Tis aan u {turn}, Waar gaade u dinkske zetten?",
                     value=f"{board['7']}{board['8']}{board['9']}\n{board['4']}{board['5']}{board['6']}\n{board['1']}{board['2']}{board['3']}")
        em.set_footer(text='Powered Eent.py', icon_url=botlogo)
        await ctx.send(embed=em)

        async def printboard(board, turn):
            new_em = discord.Embed(title=f'TicTacToe: {ctx.author} (X) VS {member} (O).', color=discord.Color.blue())
            new_em.add_field(name=f"Tis aan u {turn}, Waar gaade u dinkske zetten?",
                         value=f"{board['7']}{board['8']}{board['9']}\n{board['4']}{board['5']}{board['6']}\n{board['1']}{board['2']}{board['3']}")
            new_em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await ctx.send(embed=new_em)



        for i in range(100):

            if i != 0:
                await printboard(board,turn)

            if turn == 'X':
                try:
                    move = await self.client.wait_for('message', check=checkx,timeout=30)
                except asyncio.TimeoutError:
                    await ctx.send(f'We gaan ni blijven wachten he {ctx.author.mention}, {member.mention} is gewonnen :tada: \n Typt py tictactoe om opnieuw te spelen! ')
                    break

            elif turn == 'O':
                try:
                    move = await self.client.wait_for('message', check=checko,timeout=30)
                except asyncio.TimeoutError:
                    await ctx.send(f'We gaan ni blijven wachten he {member.mention}, {ctx.author.mention} is gewonnen :tada: \n Typt py tictactoe om opnieuw te spelen! ')
                    break

            if move.content.lower() == 'stop':
                await ctx.send('Game gestopt.')
                break
            if move.content in places:
                if board[move.content] != ':regional_indicator_o:' and board[move.content] != ':regional_indicator_x:':
                    if turn == 'X':
                        board[move.content] = ':regional_indicator_x:'
                    if turn == 'O':
                        board[move.content] = ':regional_indicator_o:'
                    count += 1
                else:
                    await ctx.send(f'verstrooid? {onsnancy} daar stond al iets')
                    continue

            else:
                await ctx.send("Das geen geldige plaats he typt de nummer van de plaats")
                continue


            if count >= 5:
                if board['7'] == board['8'] == board['9']:  # check bovenste rij
                    await ctx.send("\nGame over. \n")
                    await ctx.send("" + turn + " is gewonnen, typt py tictactoe om opnieuw te spelen!")
                    break
                elif board['4'] == board['5'] == board['6']:  # check middeste rij
                    await ctx.send("\nGame over. \n")
                    await ctx.send("" + turn + " is gewonnen, typt py tictactoe om opnieuw te spelen!")
                    break
                elif board['1'] == board['2'] == board['3']:  # check onderste rij
                    await ctx.send("\nGame over. \n")
                    await ctx.send("" + turn + " is gewonnen, typt py tictactoe om opnieuw te spelen!")
                    break
                elif board['1'] == board['4'] == board['7']:  # check linker kolom
                    await ctx.send("\nGame over. \n")
                    await ctx.send("" + turn + " is gewonnen, typt py tictactoe om opnieuw te spelen!")
                    break
                elif board['2'] == board['5'] == board['8']:  # check middeste kolom
                    await ctx.send("\nGame over. \n")
                    await ctx.send("" + turn + " is gewonnen, typt py tictactoe om opnieuw te spelen!")
                    break
                elif board['3'] == board['6'] == board['9']:  # check rechtse kolom
                    await ctx.send("\nGame over. \n")
                    await ctx.send("" + turn + " is gewonnen, typt py tictactoe om opnieuw te spelen!")
                    break
                elif board['1'] == board['5'] == board['9']:  # check diagonaal
                    await ctx.send("\nGame over. \n")
                    await ctx.send("" + turn + " is gewonnen, typt py tictactoe om opnieuw te spelen!")
                    break
                elif board['7'] == board['5'] == board['3']:  # check diagonaal2
                    await ctx.send("\nGame over. \n")
                    await ctx.send("" + turn + " is gewonnen, typt py tictactoe om opnieuw te spelen!")
                    break

            if count == 9:
                await ctx.send("\nGame over.\n")
                await ctx.send("Tis gelijk, typt py tictactoe om opnieuw te spelen!")
                break

            #van speler veranderen elke beurt
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'

    @commands.command(aliases=['4op1rij'])
    async def vieropeenrij(self, ctx, member: discord.Member = False):
        if not member:
            await ctx.send('No friends mode geactiveerd, mentiont een vriend de volgende keer (als ge da hebt)')
            member = ctx.author
        players = [ctx.author, member]
        def check(msg):
            return msg.author == players[turn%2] and msg.channel == ctx.channel


        turn = 0
        global game_over
        game_over = False
        ROW_COUNT = 6
        COLUMN_COUNT = 7

        def create_board():
            board = np.zeros((ROW_COUNT, COLUMN_COUNT))
            return board

        def draw_board(board):
            boardString = ":one::two::three::four::five::six::seven:\n"
            for r in range(ROW_COUNT):
                for c in range(COLUMN_COUNT):
                    if board[r][c] == 1:
                        boardString = boardString + ":red_circle:"
                    elif board[r][c] == 2:
                        boardString = boardString + ":yellow_circle:"
                    else:
                        boardString = boardString + ":black_circle:"
                boardString = boardString + "\n"
            return boardString

        def drop_piece(board, row, col, piece):
            board[row][col] = piece

        def is_valid_location(board, col):
            if board[ROW_COUNT - 1][col] == 0 and col <= ROW_COUNT:
                return True
            else:
                return False

        def get_next_open_row(board, col):
            for r in range(ROW_COUNT):
                if board[r][col] == 0:
                    return r

        def winning_move(board, piece):
            # Check horizontal locations for win
            for c in range(COLUMN_COUNT - 3):
                for r in range(ROW_COUNT):
                    if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                        c + 3] == piece:
                        return True

            # Check vertical locations for win
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT - 3):
                    if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                        c] == piece:
                        return True

            # Check positively sloped diaganols
            for c in range(COLUMN_COUNT - 3):
                for r in range(ROW_COUNT - 3):
                    if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                            board[r + 3][c + 3] == piece:
                        return True

            # Check negatively sloped diaganols
            for c in range(COLUMN_COUNT - 3):
                for r in range(3, ROW_COUNT):
                    if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                            board[r - 3][c + 3] == piece:
                        return True

        board = create_board()

        while not game_over:

            em = discord.Embed(title=f'vier op een rij: {ctx.author} (rood) VS {member} (geel).',
                               color=discord.Color.blue())
            em.add_field(name=f"Tis aan u {players[turn%2]}, in welke kollom gaade u dingske steken??",
                         value=draw_board(board))
            em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
            await ctx.send(embed=em)

            try:
                col = await self.client.wait_for('message', check=check, timeout=30)
            except asyncio.TimeoutError:
                if turn % 2 == 1:
                    player = ctx.author
                else:
                    player = member
                await ctx.send(f'We gaan ni blijven wachten he {players[turn%2].mention}, {player.mention} is gewonnen :tada: \n Typt py vieropeenrij om opnieuw te spelen! ')
                break


            if col.content.lower() == 'stop':
                await ctx.send('Game gestopt.')
                break

            if is_valid_location(board, int(col.content)-1):
                row = get_next_open_row(board, int(col.content)-1)
                drop_piece(board, row, int(col.content)-1, (turn%2)+1)
                if winning_move(board, (turn%2)+1):
                    em = discord.Embed(title=f'vier op een rij: {ctx.author} (rood) VS {member} (geel).',
                                       color=discord.Color.blue())
                    em.add_field(name=f"{players[turn%2]} is gewonnen! Typt py vieropeenrij om opnieuw te spelen!",
                                 value=draw_board(board))
                    em.set_footer(text='Powered by Eent.py', icon_url=botlogo)
                    await ctx.send(embed=em)
                    game_over = True
            else:
                print(1)
                if turn % 2 == 1:
                    player = ctx.author
                else:
                    player = member

                await ctx.send(f"Man man man, u pion in't bord steken he, nu is {player.mention} gewonnen")
                game_over = True
            turn += 1



async def setup(client):
    await client.add_cog(games(client))