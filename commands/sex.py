import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Sex(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def sex(self, ctx, user_1 : discord.Member):
        try:
            embed = discord.Embed(color = 0xFFA500)
            embed.add_field(name = main.get_lang(ctx.guild, "SEX_FIELD_TITLE"),value = main.get_lang(ctx.guild, "SEX_FIELD_VALUE").format(ctx.author.mention, user_1.mention))
            embed.set_footer(text = main.get_lang(ctx.guild, "COMMANDS_FOOTER").format(ctx.message.author),icon_url = ctx.message.author.avatar.url)
            await ctx.reply(embed = embed)
        except:
            embed = discord.Embed(color = 0xFFA500)
            embed.add_field(name = main.get_lang(ctx.guild, "SEX_FIELD_TITLE"),value = main.get_lang(ctx.guild, "SEX_FIELD_VALUE").format(ctx.author.mention, user_1.mention))
            embed.set_footer(text = main.get_lang(ctx.guild, "COMMANDS_FOOTER").format(ctx.message.author))
            await ctx.reply(embed = embed)            

def setup(client):
    client.add_cog(Sex(client))