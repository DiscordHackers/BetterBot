import disnake as discord
import aiohttp
import io
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Gayf(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def gayf(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        try:
            async with aiohttp.ClientSession() as jailSession:
                async with jailSession.get(f'https://api.betterbot.ru/v2/filter/gay?avatar={member.avatar.url}') as jailImg:
                    imageData = io.BytesIO(await jailImg.read())

                    await jailSession.close()

                    await ctx.reply(file = discord.File(imageData, 'gay.gif'))
        except:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "AVATAR_FIELD_VALUE1")))

def setup(client):
    client.add_cog(Gayf(client))