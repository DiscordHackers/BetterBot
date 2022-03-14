import disnake as discord
from disnake.ext import commands
from datetime import datetime
from api.server import base, main

class OnMessagEdit(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):

        if base.guild(before.guild)[6] is not None:
            if not before.author.bot:              
                embed = discord.Embed(description = main.get_lang(before.guild, "MESSAGE_EDIT"), timestamp = datetime.utcnow(), color = 0x60afff)
                embed.add_field(name = main.get_lang(before.guild, "MESSAGE_EDIT_OLD"), value=f'```{before.content}```', inline = False)
                embed.add_field(name = main.get_lang(before.guild, "MESSAGE_EDIT_NEW"), value=f'```{after.content}```', inline = False)
                embed.add_field(name = main.get_lang(before.guild, "AUTHOR"), value=before.author.mention, inline = True)
                embed.add_field(name = main.get_lang(before.guild, "CHANNEL"), value=before.channel.mention, inline = True)
                embed.set_footer(text = main.get_lang(before.guild, "MESSAGE_ID").format(before.id))
                await self.client.get_channel(int(base.guild(before.guild)[6])).send(embed = embed)

def setup(client):
    client.add_cog(OnMessagEdit(client))