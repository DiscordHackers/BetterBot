import disnake as discord
from disnake.ext import commands
from datetime import datetime
from api.server import base, main
from api.server import base

class OnMessageDelete(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        if base.guild(message.guild)[6] is not None:
            if not message.author.bot:
                try:
                    embed = discord.Embed(description = main.get_lang(message.guild, "MESSAGE_DELETE"), timestamp = datetime.utcnow(), color = 0xff6d96)
                    embed.add_field(name = main.get_lang(message.guild, "MESSAGE_DELETE_OLD"), value=f'```{message.content}```', inline = False)
                    embed.add_field(name = main.get_lang(message.guild, "AUTHOR"), value = message.author.mention, inline = True)
                    embed.add_field(name = main.get_lang(message.guild, "CHANNEL"), value = message.channel.mention, inline = True)
                    embed.set_footer(text = main.get_lang(message.guild, "MESSAGE_ID").format(message.channel.id), icon_url = message.author.avatar.url)
                    await self.client.get_channel(int(base.guild(message.guild)[6])).send(embed = embed)
                except:
                    embed = discord.Embed(description = main.get_lang(message.guild, "MESSAGE_DELETE"), timestamp = datetime.utcnow(), color = 0xff6d96)
                    embed.add_field(name = main.get_lang(message.guild, "MESSAGE_DELETE_OLD"), value=f'```{message.content}```', inline = False)
                    embed.add_field(name = main.get_lang(message.guild, "AUTHOR"), value = message.author.mention, inline = True)
                    embed.add_field(name = main.get_lang(message.guild, "CHANNEL"), value = message.channel.mention, inline = True)
                    embed.set_footer(text = main.get_lang(message.guild, "MESSAGE_ID").format(message.channel.id))
                    await self.client.get_channel(int(base.guild(message.guild)[6])).send(embed = embed)

def setup(client):
    client.add_cog(OnMessageDelete(client))