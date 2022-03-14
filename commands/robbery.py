import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
import random


class Robbery(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 3600, commands.BucketType.guild)       
    @commands.command()
    @block.block()
    async def robbery(self, ctx, user: discord.Member):
        RANDOM = random.randint(1,300)
        if (base.user(user)[6] >= int(RANDOM)):
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "ECONOMY_ROB_SUCESS").format(user.mention, RANDOM, base.guild(ctx.guild)[4])))
            base.send(f"UPDATE users SET money = money + '{RANDOM}' WHERE id = '{ctx.author.id}' AND guild = '{ctx.guild.id}'")
            base.send(f"UPDATE users SET money = money - '{RANDOM}' WHERE id = '{user.id}' AND guild = '{ctx.guild.id}'")
        else:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "ECONOMY_ROB_ERROR")))

def setup(client):
    client.add_cog(Robbery(client))
