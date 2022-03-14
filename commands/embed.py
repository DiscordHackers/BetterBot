import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def embed(self, ctx, *, body: str):
        if ctx.author.id == 874683991830183967:
            await ctx.send(f"{ctx.author.mention}, для тебя ограничено уж прости")
        else:
		
            embed = discord.Embed(description = body, color = 0x303036)
    
            await ctx.send(embed = embed)
            await ctx.message.delete()

def setup(client):
    client.add_cog(Embed(client))