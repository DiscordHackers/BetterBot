import disnake as discord
import random
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Slap(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def slap(self, ctx, member: discord.Member = None):
        slappp = [
            'https://i.gifer.com/79zo.gif',
            'https://safebooru.org/images/1882/605143df221803e99f3b5423f1df4c8b76bd8ae9.gif?1964756',
            'https://i.kym-cdn.com/photos/images/original/001/040/951/73e.gif'
        ]
        embed = discord.Embed(color=0xFFA500)
        if member != None:
            embed.description = main.get_lang(ctx.guild, "SLAP_ARGS").format(ctx.author.mention, member.mention)
        else:
            embed.description = main.get_lang(ctx.guild, "SLAP_NOARGS").format(ctx.author.mention)
        embed.set_image(url = random.choice(slappp))

        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Slap(client))