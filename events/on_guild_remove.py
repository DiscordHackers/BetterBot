from datetime import datetime
import disnake as discord
from disnake.ext import commands
from api.server import base, main


class OnGuildRemove(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        channel = self.client.get_channel(self.client.config.guildlogs)
        embed = discord.Embed(title='🔴 Бот был удалён с сервера!', description=f' ', color=0xff4444)
        embed.add_field(name='`Название сервера:`', value=f"{guild.name}", inline=False)
        embed.add_field(name='`ID сервера:`', value=guild.id, inline=False)
        embed.add_field(name='`Участников на сервере:`', value=len(guild.members), inline=False)
        embed.add_field(name='`Регион сервера:`', value=guild.region, inline=False)
        embed.add_field(name='`Серверов у бота:`', value=len(self.client.guilds), inline=False)
        await channel.send(embed=embed)
        await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f"за {len(self.client.guilds)} серверами"))


def setup(client):
    client.add_cog(OnGuildRemove(client))