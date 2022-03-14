import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
import sqlite3

connection = sqlite3.connect('data/db/main/Database.db')
cursor = connection.cursor()

class Dropdown(discord.ui.Select):
    def __init__(self, guild):
        self.guild = guild
        options = [
            discord.SelectOption(label=f"📰 {main.get_lang(guild, 'HELP_INFO')}", value="11"),
            discord.SelectOption(label=f"👦 {main.get_lang(guild, 'HELP_RP')}", value="22"),
            discord.SelectOption(label=f"😹 {main.get_lang(guild, 'HELP_FUN')}", value="33"),
            discord.SelectOption(label=f"🖼️ {main.get_lang(guild, 'HELP_IMAGE')}", value="44"),
            discord.SelectOption(label=f"🔔 {main.get_lang(guild, 'HELP_OTHER')}", value="55"),
            discord.SelectOption(label=f"⚙️ {main.get_lang(guild, 'HELP_CONFIG')}", value="66"),
            discord.SelectOption(label=f"⛏️ {main.get_lang(guild, 'HELP_MODER')}", value="77"),               
            discord.SelectOption(label=f"💰 {main.get_lang(guild, 'HELP_ECONOMY')}", value="88")                                                                
            ]
        super().__init__(
            placeholder=f"{main.get_lang(guild, 'HELP_NEED')}",
            min_values=1,
            max_values=1,
            options=options,
        )
class DropdownView(discord.ui.View):
    def __init__(self, guild):
        super().__init__()
        self.add_item(Dropdown(guild))

connection = sqlite3.connect('data/db/main/Database.db')
cursor = connection.cursor()

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['помощь', 'хелп', 'helpy', 'help-me', 'bot-help', '/хелп', '/бот-хелп', '/help'])
    @block.block()
    async def help(self, ctx):
        emb = discord.Embed(title = main.get_lang(ctx.guild, "HELP_TITLE"), description = main.get_lang(ctx.guild, "HELP_DESC").format(ctx.prefix), color = 0xFFA500)
        view=DropdownView(ctx.guild)
        await ctx.send(embed=emb, view=view)


    @commands.Cog.listener()
    async def on_dropdown(self, inter:discord.MessageInteraction):
        color = 0xff4444
        prefix = cursor.execute("SELECT prefix FROM guilds WHERE guild = {}".format(inter.guild.id)).fetchone()[0]
        embed = discord.Embed(title = main.get_lang(inter.guild, "HELP_INFO"), description = main.get_lang(inter.guild, "HELP_CATEGORY_INFO").format(prefix), color = 0xFFA500)
        embed1 = discord.Embed(title = main.get_lang(inter.guild, "HELP_RP"), description = main.get_lang(inter.guild, "HELP_CATEGORY_RP").format(prefix), color = 0xFFA500)
        embed2 = discord.Embed(title = main.get_lang(inter.guild, "HELP_FUN"), description = main.get_lang(inter.guild, "HELP_CATEGORY_FUN").format(prefix), color = 0xFFA500)
        embed3 = discord.Embed(title = main.get_lang(inter.guild, "HELP_IMAGE"), description = main.get_lang(inter.guild, "HELP_CATEGORY_IMAGE").format(prefix), color = 0xFFA500)
        embed4 = discord.Embed(title = main.get_lang(inter.guild, "HELP_OTHER"), description = main.get_lang(inter.guild, "HELP_CATEGORY_OTHER").format(prefix), color = 0xFFA500)
        embed5 = discord.Embed(title = main.get_lang(inter.guild, "HELP_CONFIG"), description = main.get_lang(inter.guild, "HELP_CATEGORY_CONFIG").format(prefix), color = 0xFFA500)
        embed6 = discord.Embed(title = main.get_lang(inter.guild, "HELP_ECONOMY"), description = main.get_lang(inter.guild, "HELP_CATEGORY_ECONOMY").format(prefix), color = 0xFFA500)
        embed7 = discord.Embed(title = main.get_lang(inter.guild, "HELP_MODER"), description = main.get_lang(inter.guild, "HELP_CATEGORY_MODER").format(prefix), color = 0xFFA500)  

        if inter.values[0] == '11':
            await inter.send(embed=embed, ephemeral=True)
        if inter.values[0] == '22':
            await inter.send(embed=embed1, ephemeral=True)
        if inter.values[0] == '33':
            await inter.send(embed=embed2, ephemeral=True)    
        if inter.values[0] == '44':
            await inter.send(embed=embed3, ephemeral=True) 
        if inter.values[0] == '55':
            await inter.send(embed=embed4, ephemeral=True)        
        if inter.values[0] == '66':
            await inter.send(embed=embed5, ephemeral=True)  
        if inter.values[0] == '77':
            await inter.send(embed=embed7, ephemeral=True) 
        if inter.values[0] == '88':
            await inter.send(embed=embed6, ephemeral=True)

def setup(client):
    client.add_cog(Help(client))