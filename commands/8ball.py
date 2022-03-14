import disnake as discord
import random
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Ball(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball', 'шар'])
    @block.block()
    async def _8ball(self, ctx, *, question: str = None):
        answer = {
            '1' : main.get_lang(ctx.guild, "8BALL_1"),
            '2' : main.get_lang(ctx.guild, "8BALL_2"),
            '3' : main.get_lang(ctx.guild, "8BALL_3"),
            '4' : main.get_lang(ctx.guild, "8BALL_4"),
            '5' : main.get_lang(ctx.guild, "8BALL_5"),
            '6' : main.get_lang(ctx.guild, "8BALL_6"),
            '7' : main.get_lang(ctx.guild, "8BALL_7"),
            '8' : main.get_lang(ctx.guild, "8BALL_8"),
            '9' : main.get_lang(ctx.guild, "8BALL_9"),
            '10' : main.get_lang(ctx.guild, "8BALL_10"),
            '11' : main.get_lang(ctx.guild, "8BALL_11"),
            '12' : main.get_lang(ctx.guild, "8BALL_12"),
            '13' : main.get_lang(ctx.guild, "8BALL_13"),
            '14' : main.get_lang(ctx.guild, "8BALL_14"),
            '15' : main.get_lang(ctx.guild, "8BALL_15"),
            '16' : main.get_lang(ctx.guild, "8BALL_16"),
        }
        if question == None:
            RANDOM = str(1)
        else:
            RANDOM = str(random.randint(2,16))

        await ctx.reply(embed = main.embed(answer[RANDOM]))


def setup(client):
    client.add_cog(Ball(client))