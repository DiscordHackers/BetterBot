import disnake as discord
from disnake.ext import commands
from datetime import datetime
from api.server import base, main

class OnMemberUpdate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_update(self, before, after):

        if base.guild(before.guild)[6] is not None:
            if not before.bot:
                if before.roles != after.roles:
                    try:
                        embed = discord.Embed(description = main.get_lang(before.guild, "MEMBER_ROLE_UPDATE").format(before.name, before.mention), timestamp = datetime.utcnow(), color = 0x00e5d6)
                        embed.add_field(name = main.get_lang(before.guild, "MEMBER_ROLE_NEW"), value = "\n".join([r.mention for r in after.roles]), inline = False)
                        embed.set_footer(text = main.get_lang(before.guild, "MEMBER_ID").format(before.id), icon_url = before.avatar.url)
                        await self.client.get_channel(int(base.guild(before.guild)[6])).send(embed = embed)
                    except:
                        embed = discord.Embed(description = main.get_lang(before.guild, "MEMBER_ROLE_UPDATE").format(before.name, before.mention), timestamp = datetime.utcnow(), color = 0x00e5d6)
                        embed.add_field(name = main.get_lang(before.guild, "MEMBER_ROLE_NEW"), value = "\n".join([r.mention for r in after.roles]), inline = False)
                        embed.set_footer(text = main.get_lang(before.guild, "MEMBER_ID").format(before.id))
                        await self.client.get_channel(int(base.guild(before.guild)[6])).send(embed = embed)                            
                elif before.name != after.name:
                    try:
                        embed = discord.Embed(description = main.get_lang(before.guild, "MEMBER_NICKNAME_UPDATE").format(before.name, before.mention), timestamp = datetime.utcnow(), color = 0x7f9bff)
                        embed.add_field(name = main.get_lang(before.guild, "MEMBER_NICKNAME_OLD"), value = before.name, inline = True)
                        embed.add_field(name = main.get_lang(before.guild, "MEMBER_NICKNAME_NEW"), value = after.name, inline = True)
                        embed.set_footer(text = main.get_lang(before.guild, "MEMBER_ID").format(before.id), icon_url = before.avatar)
                        await self.client.get_channel(int(base.guild(before.guild)[6])).send(embed = embed)
                    except:
                        embed = discord.Embed(description = main.get_lang(before.guild, "MEMBER_NICKNAME_UPDATE").format(before.name, before.mention), timestamp = datetime.utcnow(), color = 0x7f9bff)
                        embed.add_field(name = main.get_lang(before.guild, "MEMBER_NICKNAME_OLD"), value = before.name, inline = True)
                        embed.add_field(name = main.get_lang(before.guild, "MEMBER_NICKNAME_NEW"), value = after.name, inline = True)
                        embed.set_footer(text = main.get_lang(before.guild, "MEMBER_ID").format(before.id))
                        await self.client.get_channel(int(base.guild(before.guild)[6])).send(embed = embed)                        

def setup(client):
    client.add_cog(OnMemberUpdate(client))