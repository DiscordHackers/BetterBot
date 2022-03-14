import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
import random


class Work(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.cooldown(1, 1800, commands.BucketType.guild)
    @commands.command()
    @block.block()
    async def work(self, ctx):
        RANDOM = str(random.randint(501,505))
        RANDOM1 = random.randint(1,500)
        answer = {
            '501' : main.get_lang(ctx.guild, "ECONOMY_WORK_1").format(ctx.author.mention, RANDOM1, base.guild(ctx.guild)[4]),
            '502' : main.get_lang(ctx.guild, "ECONOMY_WORK_2").format(ctx.author.mention, RANDOM1, base.guild(ctx.guild)[4]),
            '503' : main.get_lang(ctx.guild, "ECONOMY_WORK_3").format(ctx.author.mention, RANDOM1, base.guild(ctx.guild)[4]),
            '504' : main.get_lang(ctx.guild, "ECONOMY_WORK_4").format(ctx.author.mention, RANDOM1, base.guild(ctx.guild)[4]),
            '505' : main.get_lang(ctx.guild, "ECONOMY_WORK_5").format(ctx.author.mention, RANDOM1, base.guild(ctx.guild)[4]),
        }        

        await ctx.reply(embed = main.embed(answer[RANDOM]))
        base.send(f"UPDATE users SET money = money + '{RANDOM1}' WHERE id = '{ctx.author.id}' AND guild = '{ctx.guild.id}'")



def setup(client):
    client.add_cog(Work(client))
