import discord
from discord.ext import commands, tasks
from config import *

from math import floor
#from replit import db
import json
import yfinance as yf
import plotly.graph_objs as go
import asyncio


class stock(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('stock is ready')
        # self.currency.start()

    """
    @tasks.loop(minutes=1)
    async def currency(self):
        try:
            db["stock"]
        except KeyError:
            db["stock"] = {"money": 572.46, "googl": 2, "currentPrice": 2219.47}
        # ask = buy
        # bid = sell
        # print("samething")
        stock = "googl"
        newdata = yf.Ticker(stock).info
        data = db['stock']
        # print(f'sell: {newdata["ask"]}, buy: {newdata["bid"]}, "currentPrice: {newdata["currentPrice"]}')
        if newdata["ask"] != 0:
            if newdata["currentPrice"] < data["currentPrice"]:
                # print(data[stock] * newdata["ask"])
                data["money"] += data[stock] * newdata["bid"]
                data[str(stock)] = 0
                # print("verkoop stocks")
    
            if newdata["currentPrice"] > data["currentPrice"]:      # als de prijs nu groter is dan de oude prijs
                buystocks = floor(data["money"] / newdata["ask"])   # bereken max aantal stocks te kopen
                # print(buystocks * newdata["ask"])
                data[stock] += buystocks                            # doe stocks bij data
                data["money"] -= buystocks * newdata["ask"]         # betaal geld voor stock
                # print("koop stocks")
    
        else:
            pass
            # print("markt is toe")
    
    
        data["currentPrice"] = newdata["currentPrice"]
    
        db["stock"] = data

    """
    @commands.command()
    async def stockinfo(self, ctx, stock):
        msg = await ctx.send("kzal is zoeke of k iet vind e")
        data = yf.Ticker(stock)
        di = data.info
        if di["regularMarketPrice"] == None:
            await msg.edit(content="Ja man, ge moet wel een stock invoeren (NASDAQ)")
        else:
            await msg.edit(content="ja kheb t, nog ff deftig doen...")
            # make fancy embed
            em = discord.Embed(title=f"aandeel info van {di['shortName']}({stock})")
            em.set_thumbnail(url=di["logo_url"])

            # add stats of the stock
            em.add_field(name="prijs", value=f"`{di['currentPrice']} $`")
            em.add_field(name="koop prijs", value=f"`{di['ask']} $`")
            em.add_field(name="verkoop prijs", value=f"`{di['bid']} $`")
            em.add_field(name=f"laagste dag", value=f"`{di['dayLow']} $`")
            em.add_field(name="hoogste dag", value=f"`{di['dayHigh']} $`")
            em.add_field(name="laagste jaar", value=f"`{di['fiftyTwoWeekLow']} $`")
            em.add_field(name="hoogste jaar", value=f"`{di['fiftyTwoWeekHigh']} $`")
            em.add_field(name="200 dag gemiddelde", value=f"`{di['twoHundredDayAverage']} $`")

            # add stock to stocks
            print(2)
            file = json.load(open("lijsten/stocks.json", "r"))
            print(3)
            try:
                print(file[di["shortName"]])
            except KeyError:
                file[di["shortName"]] = stock
                json.dump(file, open("lijsten/stocks.json", "w"))
            print(4)
            # add chard
            """
            data = yf.download(tickers=stock, period="730d", interval="1h", rounding=bool)
            print(5)
            fig = go.Figure()
            print(8)
            fig.add_trace(
                go.Candlestick(x=data.index, open=data['Open'], high=data["High"], low=data["Low"], close=data["Close"]
                               , name=f"{di['shortName']} stock history"))
            print(7)
            fig.update_layout(title=f"{di['shortName']} history", yaxis_title=f"{di['shortName']} in USD")
            print(6)
            fig.write_image(file="graph.png", engine="auto")
            print(5)
            file = discord.File("graph.png")
            print(1)
            em.set_image(url="graph.png")
            print(2)
            """
            data = yf.download(tickers=stock, period="730d", interval="1h", rounding=bool)
            print("found")
            fig = go.Figure()
            print("fig")
            fig.add_trace(go.Candlestick(x=data.index, open=data['Open'], high=data["High"], low=data["Low"], close=data["Close"], name=f"{di['shortName']} stock history"))
            print("fig config")

            fig.update_layout(title=f"{di['shortName']} history", yaxis_title=f"{di['shortName']} in USD")
            print("fig layout")
            # fig.write_image(file="graph.png", engine="kaleido")
            print("download")
            file = fig.to_image(engine="kaleido")
            print("msg")
            
            await msg.edit(file=file, content=f"", embed=em)  # file = file !!!!!


async def setup(client):
    await client.add_cog(stock(client))
