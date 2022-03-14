import disnake as discord
import requests
import json
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Wink(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def wink(self, ctx, member: discord.Member = None):
        response = requests.get('https://some-random-api.ml/animu/wink')
        json_data = json.loads(response.text)

        embed = discord.Embed(color = 0xFFA500)
        if member != None:
            embed.description = main.get_lang(ctx.guild, "WINK_ARGS").format(ctx.author.mention, member.mention)
        else:
            embed.description = main.get_lang(ctx.guild, "WINK_NOARGS").format(ctx.author.mention)
        embed.set_image(url = json_data['link'])

        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Wink(client))