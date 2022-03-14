import disnake as discord
import random
from disnake.ext import commands
from api.check import utils, block
import io
from api.server.dataIO import fileIO
from api.server import base, main


class Bot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["бот", "ботик", "ботинфо", "botinfo", "bi"])
    @block.block()
    async def bot(self, ctx):
        info = fileIO("data/db/stats.json", "load")
        serverCount = len(self.client.guilds)
        memberCount = len(set(self.client.get_all_members()))
        embed = discord.Embed( title = 'Better Information', description = main.get_lang(ctx.guild, 'BOT_TITLE').format(serverCount, memberCount, info["Commands_used"]), color = 0xFFA500)

        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Bot(client))