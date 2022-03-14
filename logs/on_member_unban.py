import disnake as discord
from disnake.ext import commands
from datetime import datetime
from api.server import base, main

class OnMemberUnBan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):

        if base.guild(guild)[6] is not None:
            async for event in guild.audit_logs(limit = 1, action = discord.AuditLogAction.unban):
                if getattr(event.target, "id", None) != user.id:
                    continue
                try:
                    embed = discord.Embed(description = main.get_lang(guild, "MEMBER_UNBAN").format(user.name, user.mention), timestamp = datetime.utcnow(), color = 0x85ea8a)
                    embed.add_field(name = main.get_lang(guild, "MODERATOR"), value=f'**{event.user.name}** ({event.user.mention})', inline = True)
                    embed.set_footer(text = main.get_lang(guild, "MEMBER_ID").format(user.id), icon_url = user.avatar.url)
                    await self.client.get_channel(int(base.guild(guild)[6])).send(embed = embed)
                except:
                    embed = discord.Embed(description = main.get_lang(guild, "MEMBER_UNBAN").format(user.name, user.mention), timestamp = datetime.utcnow(), color = 0x85ea8a)
                    embed.add_field(name = main.get_lang(guild, "MODERATOR"), value=f'**{event.user.name}** ({event.user.mention})', inline = True)
                    embed.set_footer(text = main.get_lang(guild, "MEMBER_ID").format(user.id))
                    await self.client.get_channel(int(base.guild(guild)[6])).send(embed = embed)

def setup(client):
    client.add_cog(OnMemberUnBan(client))