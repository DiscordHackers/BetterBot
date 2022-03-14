import disnake as discord
import random
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Kiss(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def kiss(self, ctx, member: discord.Member = None):
        kisss = [
            'https://data.whicdn.com/images/294084710/original.gif',
            'https://im0-tub-ru.yandex.net/i?id=891bd2b6228afa51bd76bc2c61050a17&n=13'
        ]
        embed = discord.Embed(color = 0xFFA500)
        if member != None:
            embed.description = main.get_lang(ctx.guild, "KISS_ARGS").format(ctx.author.mention, member.mention)
        else:
            embed.description = main.get_lang(ctx.guild, "KISS_NOARGS").format(ctx.author.mention)
        embed.set_image(url = random.choice(kisss))

        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Kiss(client))