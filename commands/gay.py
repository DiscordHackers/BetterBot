import disnake as discord
import random
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Gay(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def gay(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        embed = discord.Embed(color = 0xFFA500)
        embed.add_field(name = main.get_lang(ctx.guild, 'GAY_FIELD_TITLE'), value = main.get_lang(ctx.guild, 'GAY_FIELD_VALUE').format(user.mention, random.randint(1,100)))

        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Gay(client))