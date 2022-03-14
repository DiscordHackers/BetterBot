import disnake as discord
from disnake.ext import commands
from datetime import datetime
from api.server import base, main

class OnMembereRemove(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        if base.guild(member.guild)[6] is not None:
            try:
                embed = discord.Embed(description = main.get_lang(member.guild, "MEMBER_REMOVE").format(member.name, member.mention), timestamp = datetime.utcnow(), color = 0xead967)
                embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id), icon_url = member.avatar.url)
                await self.client.get_channel(int(base.guild(member.guild)[6])).send(embed = embed)
            except:
                embed = discord.Embed(description = main.get_lang(member.guild, "MEMBER_REMOVE").format(member.name, member.mention), timestamp = datetime.utcnow(), color = 0xead967)
                embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id))
                await self.client.get_channel(int(base.guild(member.guild)[6])).send(embed = embed)

        if base.guild(member.guild)[8] is not None:
            try:
                embed = discord.Embed(description = main.get_lang(member.guild, "GOODBYE_MEMBER_JOIN").format(member.mention), color = 9579219, timestamp = datetime.utcnow())
                embed.set_author(name = main.get_lang(member.guild, "GOODBYE_MEMBER_GUILD").format(member.guild.name))
                embed.set_thumbnail(url = f"{member.guild.icon}")
                embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id))
                await self.client.get_channel(int(base.guild(member.guild)[8])).send(embed = embed)
            except:
                embed = discord.Embed(description = main.get_lang(member.guild, "GOODBYE_MEMBER_JOIN").format(member.mention), color = 9579219, timestamp = datetime.utcnow())
                embed.set_author(name = main.get_lang(member.guild, "GOODBYE_MEMBER_GUILD").format(member.guild.name))
                embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id))
                await self.client.get_channel(int(base.guild(member.guild)[8])).send(embed = embed)                

def setup(client):
    client.add_cog(OnMembereRemove(client))