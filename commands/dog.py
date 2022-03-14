import disnake as discord
import requests
import json
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Dog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def dog(self, ctx):
        response = requests.get('https://some-random-api.ml/img/dog')
        json_data = json.loads(response.text)

        embed = discord.Embed(color = 0xFFA500, title = main.get_lang(ctx.guild, "DOG_TITLE"))
        embed.set_image(url = json_data['link'])

        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Dog(client))