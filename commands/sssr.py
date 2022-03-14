import disnake as discord
import aiohttp
import io
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Sssr(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def sssr(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        try:
            async with aiohttp.ClientSession() as comradeSession:
                async with comradeSession.get(f'https://api.betterbot.ru/v2/filter/comrade?avatar={member.avatar.url}') as comradeImg:
                    imageData = io.BytesIO(await comradeImg.read())

                    await comradeSession.close()

                    await ctx.reply(file = discord.File(imageData, 'comrade.gif'))
        except:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "AVATAR_FIELD_VALUE1")))

def setup(client):
    client.add_cog(Sssr(client))