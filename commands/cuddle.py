import disnake as discord
import random
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Cuddle(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def cuddle(self, ctx, member: discord.Member = None):
        cuddlee = [
            'https://data.whicdn.com/images/241295638/original.gif',
            'https://im0-tub-ru.yandex.net/i?id=26fa1e1f6e191b598ce4148c6bab699e-srl&n=13'
        ]
        embed = discord.Embed(color=0xFFA500)
        if member != None:
            embed.description = main.get_lang(ctx.guild, "CUDDLE_ARGS").format(ctx.author.mention, member.mention)
        else:
            embed.description = main.get_lang(ctx.guild, "CUDDLE_NOARGS").format(ctx.author.mention)
        embed.set_image(url = random.choice(cuddlee))

        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Cuddle(client))