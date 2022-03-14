import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
from api.check import block, support, utils

class Warn(commands.Cog):

    def __init__(self, client):
        self.client = client     

    @commands.command(aliases=['варн', 'предупреждение', 'пред', 'выдать-варн', 'выдать-пред', 'предуп'])
    @commands.has_permissions(manage_messages=True)
    async def warn(self, ctx, member: discord.Member, *, reason):
        if ctx.author.top_role.position <= member.top_role.position:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "TOP")))       
        elif member == None:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "WARN_NOARG")))
        elif member == ctx.author:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "WARN_SUICIDE")))
        elif reason == None:
            reason = ""
        else: 
            base.send(f"UPDATE users SET warn = warn + 1 WHERE id = {member.id} AND guild = {ctx.guild.id}")
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "WARN_DONE").format(ctx.author.mention, member.mention, reason, base.user(member)[5])))
            await member.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "WARN_MEMBER").format(ctx.guild.name, reason, ctx.author.mention, ctx.author.id)))
            if (base.user(member)[5] == base.guild(ctx.guild)[10]):
                if (base.guild(ctx.guild)[11] == 'mute'):
                    nakaztitle = main.get_lang(ctx.guild, "CONFIG_MUTE")
                    await ctx.guild.timeout(member, duration=86400)
                    await member.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "WARN_PUN").format(ctx.guild.name, nakaztitle)))
                    await ctx.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "WARN_MUTE").format(member.mention)))
                    base.send(f"UPDATE users SET warn = 0 WHERE id = {member.id} AND guild = {ctx.guild.id}")
                elif (base.guild(ctx.guild)[11] == 'ban'):
                    nakaztitle1 = main.get_lang(ctx.guild, "CONFIG_BAN")
                    await member.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "WARN_PUN").format(ctx.guild.name, nakaztitle1)))                    
                    await member.ban(reason=f"{main.get_lang(ctx.guild, 'WARN_REASON')}")
                    await ctx.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "WARN_BAN").format(member.mention)))
                    base.send(f"UPDATE users SET warn = 0 WHERE id = {member.id} AND guild = {ctx.guild.id}") 
                elif (base.guild(ctx.guild)[11] == 'kick'):
                    nakaztitle2 = main.get_lang(ctx.guild, "CONFIG_KICK")
                    await member.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "WARN_PUN").format(ctx.guild.name, nakaztitle2)))                    
                    await member.kick(reason=f"{main.get_lang(ctx.guild, 'WARN_REASON')}")
                    await ctx.send(embed = main.warn(ctx.guild, main.get_lang(ctx.guild, "WARN_KICK").format(member.mention)))
                    base.send(f"UPDATE users SET warn = 0 WHERE id = {member.id} AND guild = {ctx.guild.id}")

def setup(client):
    client.add_cog(Warn(client))