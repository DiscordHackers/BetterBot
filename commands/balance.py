import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Balance(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['bal', 'bank', 'money', 'бал', 'баланс', 'банк', 'деньги'])
    @block.block()
    async def balance(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        embed = discord.Embed(title = main.get_lang(ctx.guild, "BALANCE_TITLE"), description = main.get_lang(ctx.guild, "BALANCE_DESCRIPTION").format(member.mention),color = 0xFFA500)
        embed.add_field(name = main.get_lang(ctx.guild, "BALANCE_NOBUY"), value = f'{base.user(member)[6]} {base.guild(ctx.guild)[4]}')
        embed.add_field(name = main.get_lang(ctx.guild, "BALANCE_BANK"), value = f'{base.user(member)[7]} {base.guild(ctx.guild)[4]}')

        await ctx.reply(embed = embed)


def setup(client):
    client.add_cog(Balance(client))