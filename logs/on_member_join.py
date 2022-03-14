import disnake as discord
from disnake.ext import commands
from datetime import datetime
from api.server import base, main

class OnMemberJoin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):

        if base.guild(member.guild)[6] is not None:
            try:
                embed = discord.Embed(description = main.get_lang(member.guild, "MEMBER_JOIN").format(member.name, member.mention), timestamp = datetime.utcnow(), color = 0x7de848)
                embed.add_field(name = main.get_lang(member.guild, "REGISTER_DATE"), value = member.created_at.__format__('%d %B %Y'), inline = False)
                embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id), icon_url = member.avatar.url)
                await self.client.get_channel(int(base.guild(member.guild)[6])).send(embed = embed)
            except:
                embed = discord.Embed(description = main.get_lang(member.guild, "MEMBER_JOIN").format(member.name, member.mention), timestamp = datetime.utcnow(), color = 0x7de848)
                embed.add_field(name = main.get_lang(member.guild, "REGISTER_DATE"), value = member.created_at.__format__('%d %B %Y'), inline = False)
                embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id))
                await self.client.get_channel(int(base.guild(member.guild)[6])).send(embed = embed)

        if base.guild(member.guild)[7] is not None:
            try:            
                embed = discord.Embed(description = main.get_lang(member.guild, "WELCOME_MEMBER_JOIN").format(member.mention, member.guild.name), color = 9579219, timestamp = datetime.utcnow())
                embed.set_author(name = main.get_lang(member.guild, "WELCOME_MEMBER_GUILD").format(member.guild.name))
                embed.set_thumbnail(url = f"{member.guild.icon}")
                embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id))
                await self.client.get_channel(int(base.guild(member.guild)[7])).send(embed = embed)
            except:
                embed = discord.Embed(description = main.get_lang(member.guild, "WELCOME_MEMBER_JOIN").format(member.mention, member.guild.name), color = 9579219, timestamp = datetime.utcnow())
                embed.set_author(name = main.get_lang(member.guild, "WELCOME_MEMBER_GUILD").format(member.guild.name))
                embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id))
                await self.client.get_channel(int(base.guild(member.guild)[7])).send(embed = embed)

def setup(client):
    client.add_cog(OnMemberJoin(client))