import disnake as discord
import inspect
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Source(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    @utils.developer()
    async def source(self, ctx, command):

        source = inspect.getsource(self.client.get_command(command).callback)
        if not source:
            return await ctx.reply(f'{command} не действительная команда')
        try:
            await ctx.reply(f'```py\n{source}\n```')
        except:
            paginated_text = utils.paginate(source)
            for page in paginated_text:
                if page == paginated_text[-1]:
                    await ctx.reply(f'```py\n{page}\n```')
                    break
                await ctx.reply(f'```py\n{page}\n```')


def setup(client):
    client.add_cog(Source(client))