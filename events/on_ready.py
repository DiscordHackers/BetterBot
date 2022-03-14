from datetime import datetime
import disnake as discord
import random
from disnake.ext import commands, tasks
from configs.config import status
from api.server import base, main
import psutil
import datetime, time


class OnReady(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = f"help | client"))
        print("ptero start") # ? Для того чтобы Pterodactyl что сервер прошел инициализацию и уже запущен
        self.client.logger('Успешно подключился к серверам Discord', 'ready')
        self.client.logger(f'Имя: {self.client.user.name}', 'ready')
        self.client.logger(f'ID: {self.client.user.id}' , 'ready')
        global startTime
        startTime = time.time()        
        self.status_task.start()
        
        #for guild in self.client.guilds:
        #    print(guild.id , guild.name)

        channel = self.client.get_channel(self.client.config.versionid)
        await channel.edit(name = f'{self.client.config.versionname} {self.client.version}')

                        
    @commands.command(name='stats')
    async def _stats(self,ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        memory = psutil.virtual_memory().total / (1024.0 ** 3)
        await ctx.send(embed = discord.Embed(title = 'Информация', description = f'``` • Пинг          :: {round(self.client.latency * 1000)} \n • ОЗУ исп.      :: {round(memory)} MB \n • Аптайм бота   :: {uptime} \n\n • disnake       :: v{discord.__version__} \n • Версия бота   :: {self.client.version} ```'))                                                 

    @tasks.loop(minutes = 0.2)
    async def status_task(self):
        await self.client.change_presence(activity = discord.Game(random.choice(self.client.config.status)))

def setup(client):
    client.add_cog(OnReady(client))