import disnake as discord
import random
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Penis(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def penis(self, ctx, user: discord.Member = None):
        santimetrs = [
            '=',
            '==',
            '===',
            '====',
            '=====',
            '======',
            '=======',
            '========',
            '=========',
            '==========',
            '===========',
            '============',
            '=============',
            '==============',
            '===============',
            '================',
            '=================',
            '==================',
            '===================',
            '====================',
            '=====================',
            '======================',
        ]
        if not user:
            user = ctx.author

        try:
            embed = discord.Embed(color = 0xFFA500)
            embed.add_field(name = main.get_lang(ctx.guild, "PENIS_FIELD_TITLE"),value = main.get_lang(ctx.guild, "PENIS_FIELD_VALUE").format(user.mention, random.choice(santimetrs)))
            embed.set_footer(text = main.get_lang(ctx.guild, "COMMANDS_FOOTER").format(ctx.message.author),icon_url = ctx.message.author.avatar.url)
            await ctx.reply(embed = embed)
        except:
            embed = discord.Embed(color = 0xFFA500)
            embed.add_field(name = main.get_lang(ctx.guild, "PENIS_FIELD_TITLE"),value = main.get_lang(ctx.guild, "PENIS_FIELD_VALUE").format(user.mention, random.choice(santimetrs)))
            embed.set_footer(text = main.get_lang(ctx.guild, "COMMANDS_FOOTER").format(ctx.message.author))
            await ctx.reply(embed = embed)            

def setup(client):
    client.add_cog(Penis(client))