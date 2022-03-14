import disnake as discord
import uuid
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Key(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def key( self, ctx ):
        embed = discord.Embed(title = 'Случайный сгенерированный ключ', color=0xFFA500)

        embed.add_field( name = '** **', value = f"{uuid.uuid4()}", inline = False )
        await ctx.reply( embed = embed )


def setup(client):
    client.add_cog(Key(client))