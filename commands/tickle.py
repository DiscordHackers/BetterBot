import disnake as discord
import random
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Tickle(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def tickle(self, ctx, member: discord.Member = None):
        tickkle = [
            'https://i.gifer.com/KVjQ.gif',
            'https://i.gifer.com/O4QR.gif'
        ]
        embed = discord.Embed(color = 0xFFA500)
        if member != None:
            embed.description = main.get_lang(ctx.guild, "TICKLE_ARGS").format(ctx.author.mention, member.mention)
        else:
            embed.description = main.get_lang(ctx.guild, "TICKLE_NOARGS").format(ctx.author.mention)
        embed.set_image(url = random.choice(tickkle))

        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Tickle(client))