import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
from api.check import block, support, utils

class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client     

    @commands.cooldown(1, 60, commands.BucketType.guild)       
    @commands.command(aliases=['мут', 'затычка', 'заткнуть', 'выдать-мут', 'мутик', 'mute-member', 'membermute', 'member-mute', 'мьют'])
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member, time, *, reason):
        time_conversion = {
            "s": 1, 
            "m": 60, 
            "h": 3600, 
            "d": 86400, 
            "с": 1, 
            "м": 60, 
            "ч": 3600, 
            "д": 86400,
        }
        mute_time = int(time[0]) * time_conversion[time[-1]]
        if ctx.author.top_role.position <= member.top_role.position:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "TOP")))        
        elif member == None:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MUTE_NOARG")))
        elif member == ctx.author:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MUTE_AUTHOR")))
        elif reason == None:
            reason = ''
        else:
            try: 
                await member.timeout(duration=mute_time, reason=f'{reason} ({ctx.author})')   
                await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "MUTE_SUCCESS").format(member.mention, ctx.author.mention, reason, time)))
                await member.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "MUTE_MEMBER").format(ctx.guild.name, ctx.author, reason, time)))
            except:
                await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "MUTE_ERROR")))

def setup(client):
    client.add_cog(Mute(client))        