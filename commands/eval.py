import disnake as discord, contextlib, io, textwrap, asyncio, aiohttp, os, sys, time, datetime, random, requests
from disnake.ext import commands, tasks
from traceback import format_exception
from api.check import utils, block
from api.server import base, main



class Eval(commands.Cog):

    def __init__(self, client):
        self.client = client

    def clean_code(self, content):
        if content.startswith("```") and content.endswith("```"):
            return "\n".join(content.split("\n")[1:])[:-3]
        else:
            return content

    @commands.command(aliases = ['exec'])
    @utils.developer()
    async def __evel(self, ctx, *, code):
        code = self.clean_code(code)

        local_variables = {
            "discord": discord,
            "commands": commands,
            "client": self.client,
            "tasks": tasks,
            "ctx": ctx,
            "asyncio": asyncio,
            "aiohttp": aiohttp,
            "os": os,
            'sys': sys,
            "time": time,
            "datetime": datetime,
            "random": random,
            "requests": requests,
            "base": base,
            "main": main,
            "channel": ctx.channel,
            "author": ctx.author,
            "guild": ctx.guild,
            "message": ctx.message,
        }

        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
                )

                obj = await local_variables["func"]()
                result = f"{stdout.getvalue()}\n-- {obj}\n"
        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        await ctx.reply(result)


def setup(client):
    client.add_cog(Eval(client))