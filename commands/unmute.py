import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
from api.check import block, support, utils

class Unmute(commands.Cog):

    def __init__(self, client):
        self.client = client     

    @commands.cooldown(1, 60, commands.BucketType.guild)       
    @commands.command(aliases=['анмут', 'анмьют', 'снять-мут', 'размутик', 'unmute-member', 'memberunmute', 'member-unmute', 'размьют'])
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        if ctx.author.top_role.position <= member.top_role.position:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "TOP")))        
        elif member == None:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "UNMUTE_NOARG")))
        elif member == ctx.author:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "UNMUTE_AUTHOR")))
        else:
                await member.timeout(duration=None)   
                await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "UNMUTE_SUCCESS").format(member.mention, ctx.author.mention)))
                await member.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "UNMUTE_MEMBER").format(ctx.guild.name, ctx.author)))

def setup(client):
    client.add_cog(Unmute(client))        