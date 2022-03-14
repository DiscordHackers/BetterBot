import disnake as discord
import sqlite3
from disnake.ext import commands
from datetime import datetime
from api.server import base, main

class OnMemberBan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):

        if base.guild(guild)[6] is not None:
            async for event in guild.audit_logs(limit = 1, action = discord.AuditLogAction.ban):
                if getattr(event.target, "id", None) != user.id:
                    continue
                try:
                    embed = discord.Embed(description = main.get_lang(guild, "MEMBER_BAN").format(user.name, user.mention), timestamp = datetime.utcnow(), color = 0xff686b)
                    embed.add_field(name = main.get_lang(guild, "MODERATOR"), value = f'**{event.user.name}** ({event.user.mention})', inline = True)
                    #embed.add_field(main.get_lang(guild, "CHANNEL"), value = f'**{channel}** ({channel.mention})', inline=True)
                    embed.add_field(name = main.get_lang(guild, "REASON"), value = event.reason, inline = True)
                    embed.set_footer(text = main.get_lang(guild, "MEMBER_ID").format(user.id), icon_url = user.avatar.url)
                    await self.client.get_channel(int(base.guild(guild)[6])).send(embed = embed)
                except:
                    embed = discord.Embed(description = main.get_lang(guild, "MEMBER_BAN").format(user.name, user.mention), timestamp = datetime.utcnow(), color = 0xff686b)
                    embed.add_field(name = main.get_lang(guild, "MODERATOR"), value = f'**{event.user.name}** ({event.user.mention})', inline = True)
                    #embed.add_field(main.get_lang(guild, "CHANNEL"), value = f'**{channel}** ({channel.mention})', inline=True)
                    embed.add_field(name = main.get_lang(guild, "REASON"), value = event.reason, inline = True)
                    embed.set_footer(text = main.get_lang(guild, "MEMBER_ID").format(user.id))
                    await self.client.get_channel(int(base.guild(guild)[6])).send(embed = embed)

def setup(client):
    client.add_cog(OnMemberBan(client))