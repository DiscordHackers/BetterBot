import disnake as discord
from disnake.ext import commands
from datetime import datetime
from api.server import base, main

class OnVoiceStateUpdate(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        if base.guild(member.guild)[6] is not None:
	        if not member.bot:
	        	if before.channel is None and after.channel is not None:
		            embed = discord.Embed(description = main.get_lang(member.guild, "MEMBER_VOICE_JOIN").format(member.name, member.mention, after.channel.name, after.channel.mention), timestamp = datetime.utcnow(), color = 0xae84e8)
		            embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id))
		            await self.client.get_channel(int(base.guild(member.guild)[6])).send(embed = embed)
	        	elif before.channel is not None and after.channel is None:
		            embed = discord.Embed(description = main.get_lang(member.guild, "MEMBER_VOICE_LEFT").format(member.name, member.mention, before.channel.name,before.channel.mention), timestamp = datetime.utcnow(), color = 0xe5aca0)
		            embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id))
		            await self.client.get_channel(int(base.guild(member.guild)[6])).send(embed = embed)
	        	elif before.channel is not None and after.channel is not None and (before.channel != after.channel):
		            embed = discord.Embed(description = main.get_lang(member.guild, "MEMBER_VOICE_SELECT").format(member.name, member.mention), timestamp = datetime.utcnow(), color = 0xae84e8)
		            embed.add_field(name = main.get_lang(member.guild, "CHANNEL"), value = after.channel.mention, inline = True)
		            embed.add_field(name = main.get_lang(member.guild, "CHANNEL_OLD"), value = before.channel.mention, inline = True)
		            embed.set_footer(text = main.get_lang(member.guild, "MEMBER_ID").format(member.id))
		            await self.client.get_channel(int(base.guild(member.guild)[6])).send(embed = embed)

def setup(client):
    client.add_cog(OnVoiceStateUpdate(client))