import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
from api.check import block, support, utils

class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client     

    @commands.cooldown(1, 300, commands.BucketType.guild)       
    @commands.command(aliases=['бан', 'забанить', 'заблокировать'])
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason):
        if ctx.author.top_role.position <= member.top_role.position:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "TOP")))        
        elif member == None:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "BAN_NOARG")))
        elif member == ctx.author:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "BAN_AUTHOR")))
        else:
            await member.ban(reason=f'{reason} ({ctx.author})')   
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "BAN_SUCCESS").format(member.mention, ctx.author.mention, reason)))
            await member.send(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "BAN_MEMBER").format(ctx.guild.name, ctx.author, reason)))
            

def setup(client):
    client.add_cog(Ban(client))        