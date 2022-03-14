import disnake as discord
import asyncio
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main


class Kill(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @block.block()
    async def kill( self, ctx, member: discord.Member ):
        embed = discord.Embed(title = 'Убийство', description = 'Вы сможете кого-то убить', colour = discord.Color.red())

        embed.add_field( name = '**Доставание дробовика**', value = f"{ctx.author.mention} достаёт дробовик...", inline = False )

        await asyncio.sleep( 3 )
        embed.add_field( name = '**Направление дробовика**', value = f"{ctx.author.mention} направляет дробовик на {member.mention}...", inline = False )

        await asyncio.sleep( 2 )
        embed.add_field( name = '**Стрельба**', value = f"{ctx.author.mention} стреляет в {member.mention}...", inline = False )

        embed.set_image(url='https://media.discordapp.net/attachments/690222948283580435/701494203607416943/tenor_3.gif')

        await asyncio.sleep( 2 )
        embed.add_field( name = '**Кровь**', value = f"{member.mention} истекает кровью...", inline = False )

        await asyncio.sleep( 3 )
        embed.add_field( name = '**Погибание**', value = f"{member.mention} погиб...", inline = False )

        await ctx.reply( embed = embed )


def setup(client):
    client.add_cog(Kill(client))