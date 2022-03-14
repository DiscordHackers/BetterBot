import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
import random


class Economy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def deposit(self, ctx, amount):
        if (int(amount) <= 0):
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "ECONOMY_BANK_ZERO").format(amount)))
        else: 
            if (base.user(ctx.author)[6] >= int(amount)):
                await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "ECONOMY_DEPOSIT_SUCESS").format(amount, base.guild(ctx.guild)[4])))
                base.send(f"UPDATE users SET money = money - '{amount}' WHERE id = '{ctx.author.id}' AND guild = '{ctx.guild.id}'")
                base.send(f"UPDATE users SET bank = bank + '{amount}' WHERE id = '{ctx.author.id}' AND guild = '{ctx.guild.id}'")
            else:
                await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "ECONOMY_DEPOSIT_ERROR")))

def setup(client):
    client.add_cog(Economy(client))
