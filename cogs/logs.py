import disnake as discord
from disnake.ext import commands
from datetime import datetime


logs_guild = False # Логирования гильдий ([on_guild_join] и [on_guild_remove]) [Фалн находится в директории (.\data\logs) ]
logs_member = False # Логирование пользователей ([on_member_join] и [on_member_remove]) [Фалн находится в директории (.\data\logs) ]
logs_guildschat = False #Логирование чата с гильдии (on_message) [Фалн находится в директории (.\data\logs\guilds) ]


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.client.logger(self.__class__.__name__, 'cogs')
    
   	#MEMEBR JOIN
    @commands.Cog.listener()
    async def on_member_join(self, member):
        if logs_member:
            timeshtamp = datetime.now().replace(microsecond = 0)
            serverid = member.guild.id
            servername = member.guild

            with open(f"data/logs/on_member_join.log", "a", encoding = "utf-8") as file:
                file.write(f"[{timeshtamp}] Был зарегестрирован пользователь {member}. ID сервера: `{serverid}`. Название сервера: `{servername}`. Путем ивента on_member_join\n")
        else:
            pass

        
    #MEMBER LEAVE
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if logs_member:
            timeshtamp = datetime.now().replace(microsecond = 0)
            
            with open(f"data/logs/on_member_remove.log", "a", encoding = "utf-8") as file:
                file.write(f"[{timeshtamp}] Был удалён пользователь {member}. Путем ивента on_member_remove\n")
        else:
            pass
    

    #GUILD JOIN
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if logs_guild:
            timeshtamp = datetime.now().replace(microsecond = 0)
            serverid = guild.id
            servername = guild.name

            with open(f"data/logs/on_guild_join.log", "a", encoding = "utf-8") as file:
                file.write(f"[{timeshtamp}]  Бот был добавлен на сервер. Название сервера: {servername}. ID сервера: {serverid}. Участников на сервере: {len(guild.members)}. Серверов у бота: {len(self.client.guilds)}\n")
        else:
            pass


    #GUILD REMOVE
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        if logs_guild:
            timeshtamp = datetime.now().replace(microsecond = 0)
            serverid = guild.id
            servername = guild.name

            with open(f"data/logs/on_guild_remove.log", "a", encoding = "utf-8") as file:
                file.write(f"[{timeshtamp}] Бот был удалён с сервера. Название сервера: {servername}. ID сервера: {serverid}. Участников на сервере: {len(guild.members)}. Серверов у бота: {len(self.client.guilds)}\n")
        else:
            pass

        
    #MESSAGE
    @commands.Cog.listener()
    async def on_message(self, message):
        if logs_guildschat:
            timeshtamp = datetime.now().replace(microsecond = 0)
            
            with open(f"data/logs/guilds/{message.guild.id}_on_message.log", "a", encoding = "utf-8") as file:
                    file.write(f"Пользвоатель {message.author} написал: [ {message.content} ]\n")
        else:
            pass

        
def setup(client):
    client.add_cog(Logs(client))