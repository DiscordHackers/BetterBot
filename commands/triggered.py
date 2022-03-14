import disnake as discord
import aiohttp
import io
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Triggered(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def triggered(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        try:
            async with aiohttp.ClientSession() as trigSession:
                async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar.url}') as trigImg:
                    imageData = io.BytesIO(await trigImg.read())

                    await trigSession.close()

                    await ctx.reply(file = discord.File(imageData, 'triggered.gif'))
        except:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "AVATAR_FIELD_VALUE1")))

def setup(client):
    client.add_cog(Triggered(client))