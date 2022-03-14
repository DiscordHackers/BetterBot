import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
from api.check import block, support, utils

class Unwarn(commands.Cog):

    def __init__(self, client):
        self.client = client     

    @commands.command(aliases=['снять-предупреждение', 'анварн', 'унварн'])
    @commands.has_permissions(manage_messages=True)
    async def unwarn(self, ctx, member: discord.Member):
        if ctx.author.top_role.position <= member.top_role.position:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "TOP")))        
        elif member == None:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "WARN_NOARG")))
        elif member == ctx.author:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "UNWARN_ERROR")))
        elif base.user(member)[5] <= 0:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "UNWARN_ZEROW")))
        else:   
            base.send(f"UPDATE users SET warn = warn - 1 WHERE id = {member.id} AND guild = {ctx.guild.id}")
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "UNWARN_DONE").format(ctx.author.mention, member.mention, base.user(member)[5])))

def setup(client):
    client.add_cog(Unwarn(client))        