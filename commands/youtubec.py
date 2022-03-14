import disnake as discord
import urllib
from disnake.ext import commands
from urllib.parse import quote
from api.check import utils, block
from api.server import base, main


class Youtubec(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def comment(self, ctx, *, comment, member = None):
        if not member:
            member = ctx.author
        try:
            embed = discord.Embed(color = 0xFFA500)
            embed.set_image(url = f'https://some-random-api.ml/canvas/youtube-comment?avatar={member.avatar.url}&username={quote(member.name)}&comment={quote(comment)}')
            await ctx.reply(embed = embed)
        except:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "AVATAR_FIELD_VALUE1")))

def setup(client):
    client.add_cog(Youtubec(client))