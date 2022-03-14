import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Guildlist(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @utils.developer()
    @block.block()
    async def guildlist(self, ctx):
        for guild in self.client.guilds:
            print(guild.id , guild.name)


def setup(client):
    client.add_cog(Guildlist(client))