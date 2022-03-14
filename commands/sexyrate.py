import disnake as discord
import random
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class SexyRate(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def sexyrate(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        try:
            embed = discord.Embed(color = 0xFFA500)
            embed.add_field(name = main.get_lang(ctx.guild, "SEXYRATE_FIELD_TITLE"),value = main.get_lang(ctx.guild, "SEXYRATE_FIELD_VALUE").format(random.randint(1,100)))
            embed.set_thumbnail(url = member.avatar.url)
            embed.set_footer(text = main.get_lang(ctx.guild, "COMMANDS_FOOTER").format(ctx.message.author),icon_url = ctx.message.author.avatar.url)
            await ctx.reply(embed = embed)
        except:
            embed = discord.Embed(color = 0xFFA500)
            embed.add_field(name = main.get_lang(ctx.guild, "SEXYRATE_FIELD_TITLE"),value = main.get_lang(ctx.guild, "SEXYRATE_FIELD_VALUE").format(random.randint(1,100)))
            embed.set_footer(text = main.get_lang(ctx.guild, "COMMANDS_FOOTER").format(ctx.message.author))
            await ctx.reply(embed = embed)

def setup(client):
    client.add_cog(SexyRate(client))