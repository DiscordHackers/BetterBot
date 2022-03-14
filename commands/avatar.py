import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ["аватар", "аватарка", "avatarka", "ава", "авотарка", "ava"])
    @block.block()
    async def avatar(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author

        try:
            embed = discord.Embed(color = discord.Color.blue())
            embed.add_field(name = main.get_lang(ctx.guild, 'AVATAR_FIELD_TITLE'),value = main.get_lang(ctx.guild, 'AVATAR_FIELD_VALUE').format(member.mention),inline = False)
            embed.set_image(url = member.avatar)
            embed.set_footer(text = main.get_lang(ctx.guild, 'COMMANDS_FOOTER').format(ctx.message.author),icon_url = ctx.message.author.avatar)
            await ctx.send(embed = embed)
        except:
            embed = discord.Embed(color = discord.Color.blue())
            embed.add_field(name = main.get_lang(ctx.guild, 'AVATAR_FIELD_TITLE'),value = main.get_lang(ctx.guild, 'AVATAR_FIELD_VALUE1').format(member.mention),inline = False)
            embed.set_footer(text = main.get_lang(ctx.guild, 'COMMANDS_FOOTER').format(ctx.message.author))
            await ctx.send(embed = embed)            


def setup(client):
    client.add_cog(Avatar(client))