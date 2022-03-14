import sqlite3
import psutil
import disnake as discord
from disnake.ext import commands
from disnake.ext.commands import bot, check, MissingPermissions, has_permissions
from disnake.utils import get
from os import listdir

from util.logger import Logger

from api.server.dataIO import fileIO
from api.check import block, support, utils
from api.server import base, main
from configs import config

# ? ------------------------
# ? | SETUP DISCORD CLIENT |
# ? ------------------------

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.guilds = True
intents.messages = True

async def get_prefix(client, message):
    connection = sqlite3.connect('data/db/main/Database.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM guilds WHERE guild = {message.guild.id}")
    result = cursor.fetchone()
    return result[2]

client = commands.Bot(
    command_prefix = get_prefix,
    help_command = None,
    intents = discord.Intents.all()
)

# ? ----------------
# ? | LOADING COGS |
# ? ----------------

for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

for filename in listdir('./commands/'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')
    else:
        if (filename != '__pycache__'):
            for file in listdir(f'./commands/{filename}/'):
                if file.endswith('.py'):
                    client.load_extension(f'commands.{filename}.{file[:-3]}')

for filename in listdir('./events/'):
    if filename.endswith('.py'):
        client.load_extension(f'events.{filename[:-3]}')

for filename in listdir('./logs/'):
    if filename.endswith('.py'):
        client.load_extension(f'logs.{filename[:-3]}')

# ? --------------------
# ? | BOT DEV CATEGORY |
# ? --------------------

@client.slash_command()
async def bot(inter):
    memory = psutil.virtual_memory().total / (1024.0 ** 3)
    send = inter.response.send_message
    await send(embed = discord.Embed(title = 'Информация', description = f'``` • Пинг          :: {round(client.latency * 1000)} \n • ОЗУ исп.      :: {round(memory)} MB \n\n • disnake       :: v{discord.__version__} \n • Версия бота   :: {client.version} ```'))         

@client.event
async def on_command(command):
	info = fileIO("data/db/stats.json", "load")
	info["Commands_used"] = info["Commands_used"] + 1
	fileIO("data/db/stats.json", "save", info)

# * ----------------

@client.command()
@utils.developer()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Модуль `{extension}` был загружен"))

@client.command()
@utils.developer()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Модуль `{extension}` был отключен"))

@client.command()
@utils.developer()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Модуль `{extension}` был перезагружен"))
    
# * ----------------

@client.command()
@utils.developer()
async def cload(ctx, extension):
    client.load_extension(f"commands.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Команда `{extension}` была включена"))


@client.command()
@utils.developer()
async def cunload(ctx, extension):
    client.unload_extension(f"commands.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Команда `{extension}` была отключена"))


@client.command()
@utils.developer()
async def creload(ctx, extension):
    client.reload_extension(f"commands.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Команда `{extension}` была перезагружена"))

# * ----------------

@client.command()
@utils.developer()
async def eload(ctx, extension):
    client.load_extension(f"events.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Событие `{extension}` было включено"))

@client.command()
@utils.developer()
async def eunload(ctx, extension):
    client.unload_extension(f"events.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Событие `{extension}` было отключено"))

@client.command()
@utils.developer()
async def ereload(ctx, extension):
    client.reload_extension(f"events.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Событие `{extension}` было перезагружено"))

# * ----------------

@client.command()
@utils.developer()
async def lload(ctx, extension):
    client.load_extension(f"logs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Лог `{extension}` был загружен"))

@client.command()
@utils.developer()
async def lunload(ctx, extension):
    client.unload_extension(f"logs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Лог `{extension}` был отключен"))

@client.command()
@utils.developer()
async def lreload(ctx, extension):
    client.reload_extension(f"logs.{extension}")
    await ctx.reply(embed = main.done(ctx.guild, f"Лог `{extension}` был  перезагружен"))
    
# ? -----------------
# ? | UTIL CATEGORY |
# ? -----------------

client.version = config.version
client.logger = Logger
client.config = config

# ? --------------------
# ? | BOT REGISTRATION |
# ? --------------------

client.run(config.token)