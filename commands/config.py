import disnake as discord
import os
from disnake.ext import commands
from datetime import datetime
from disnake.utils import get
from configs.config import prefix, lang, currency
from api.check import utils, block
from api.server import base, main
from os import listdir
import sqlite3

class Dropdown(discord.ui.Select):
    def __init__(self, guild):
        self.guild = guild
        options = [
            discord.SelectOption(label=f"⚙️ {main.get_lang(guild, 'CONFIG1')}", value="1"),
            discord.SelectOption(label=f"🌍 {main.get_lang(guild, 'CONFIG2')}", value="2"),
            discord.SelectOption(label=f"🎭 {main.get_lang(guild, 'CONFIG3')}", value="3"),
            discord.SelectOption(label=f"👋 {main.get_lang(guild, 'CONFIG4')}", value="4"),
            discord.SelectOption(label=f"👋 {main.get_lang(guild, 'CONFIG5')}", value="5"),
            discord.SelectOption(label=f"📝 {main.get_lang(guild, 'CONFIG6')}", value="6"),
            discord.SelectOption(label=f"⬆️ {main.get_lang(guild, 'CONFIG7')}", value="7"),
            discord.SelectOption(label=f"💰 {main.get_lang(guild, 'CONFIG8')}", value="8"),
            discord.SelectOption(label=f"⛏️ {main.get_lang(guild, 'CONFIG9')}", value="9"),
            discord.SelectOption(label=f"⛏️ {main.get_lang(guild, 'CONFIG10')}", value="10")                                                                    
            ]
        super().__init__(
            placeholder=f"{main.get_lang(guild, 'CONFIG_NEED')}",
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

class Config(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command = True)
    @commands.has_permissions(administrator = True)
    @block.block()
    async def config(self, ctx):
        try:
            if base.guild(ctx.guild)[7] is not None:
                channel = self.client.get_channel(base.guild(ctx.guild)[7])
                welcome = main.get_lang(ctx.guild, "CONFIG_WELCOME").format(channel.mention)
            else:
                welcome = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[welcome]`'

            if base.guild(ctx.guild)[6] is not None:
                channel = self.client.get_channel(base.guild(ctx.guild)[6])
                logs = main.get_lang(ctx.guild, "CONFIG_LOGS").format(channel.mention)
            else:
                logs = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[logs]`'

            if base.guild(ctx.guild)[8] is not None:
                channel = self.client.get_channel(base.guild(ctx.guild)[8])
                goodbuy = main.get_lang(ctx.guild, "CONFIG_GOODBYE").format(channel.mention)
            else:
                goodbuy = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[goodbye]`'
            
            if base.guild(ctx.guild)[9] is not None:
                channel = self.client.get_channel(base.guild(ctx.guild)[9])
                lvl = main.get_lang(ctx.guild, "CONFIG_LVL").format(channel.mention)
            else:
                lvl = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[lvl]`'            

            if base.guild(ctx.guild)[5] is not None:
                role = get(ctx.guild.roles, id = base.guild(ctx.guild)[5])
                autorole =  main.get_lang(ctx.guild, "CONFIG_AUTOROLE").format(role.mention)
            else:
                autorole = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[autorole]`'

            if base.guild(ctx.guild)[2] != ".":
                prefix =  main.get_lang(ctx.guild, "CONFIG_PREFIX").format(ctx.prefix)
            else:
                prefix = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[prefix]`'

            if base.guild(ctx.guild)[3] != "ru":
                lang =  main.get_lang(ctx.guild, "CONFIG_LANG").format(base.guild(ctx.guild)[3])
            else:
                lang = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[lang]`'
                                  
            if base.guild(ctx.guild)[4] != "<:better_moneyb:937110288807907378>":
                cur =  main.get_lang(ctx.guild, "CONFIG_CURRENCY").format(base.guild(ctx.guild)[4])
            else:
                cur = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[currency]`'  
            if base.guild(ctx.guild)[10] != 3:
                warnl = main.get_lang(ctx.guild, "CONFIG_WARNCOUNT").format(base.guild(ctx.guild)[10])               
            else: 
                warnl = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[warn]`'    
            if base.guild(ctx.guild)[11] != "mute":
                if base.guild(ctx.guild)[11] == "mute":
                    nakaztitle = f'{main.get_lang(ctx.guild, "CONFIG_MUTE")}'
                elif base.guild(ctx.guild)[11] == "kick":
                    nakaztitle = f'{main.get_lang(ctx.guild, "CONFIG_KICK")}'
                elif base.guild(ctx.guild)[11] == "ban":
                    nakaztitle = f'{main.get_lang(ctx.guild, "CONFIG_BAN")}'
                nakaz = main.get_lang(ctx.guild, "CONFIG_WARNPUN").format(nakaztitle)
            else:           
                nakaz = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[warnpun]`'
            
            emb = discord.Embed(description = f'{main.get_lang(ctx.guild, "CONFIG_TITLE")} \n\n {prefix} \n {lang} \n {autorole} \n {welcome} \n {goodbuy} \n {logs} \n {lvl} \n {cur} \n {warnl} \n {nakaz}', color = 0xFFA500)
            emb.set_footer(text = main.get_lang(ctx.guild, "CONFIG_FOOTER").format(ctx.prefix),icon_url = ctx.guild.icon.url)
            view=DropdownView(ctx.guild)
            await ctx.send(embed=emb, view=view)
        except:
            if base.guild(ctx.guild)[7] is not None:
                channel = self.client.get_channel(base.guild(ctx.guild)[7])
                welcome = main.get_lang(ctx.guild, "CONFIG_WELCOME").format(channel.mention)
            else:
                welcome = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[welcome]`'

            if base.guild(ctx.guild)[6] is not None:
                channel = self.client.get_channel(base.guild(ctx.guild)[6])
                logs = main.get_lang(ctx.guild, "CONFIG_LOGS").format(channel.mention)
            else:
                logs = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[logs]`'

            if base.guild(ctx.guild)[8] is not None:
                channel = self.client.get_channel(base.guild(ctx.guild)[8])
                goodbuy = main.get_lang(ctx.guild, "CONFIG_GOODBYE").format(channel.mention)
            else:
                goodbuy = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[goodbye]`'
            
            if base.guild(ctx.guild)[9] is not None:
                channel = self.client.get_channel(base.guild(ctx.guild)[9])
                lvl = main.get_lang(ctx.guild, "CONFIG_LVL").format(channel.mention)
            else:
                lvl = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[lvl]`'            

            if base.guild(ctx.guild)[5] is not None:
                role = get(ctx.guild.roles, id = base.guild(ctx.guild)[5])
                autorole =  main.get_lang(ctx.guild, "CONFIG_AUTOROLE").format(role.mention)
            else:
                autorole = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[autorole]`'

            if base.guild(ctx.guild)[2] != ".":
                prefix =  main.get_lang(ctx.guild, "CONFIG_PREFIX").format(ctx.prefix)
            else:
                prefix = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[prefix]`'

            if base.guild(ctx.guild)[3] != "ru":
                lang =  main.get_lang(ctx.guild, "CONFIG_LANG").format(base.guild(ctx.guild)[3])
            else:
                lang = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[lang]`'
                                  
            if base.guild(ctx.guild)[4] != "<:better_moneyb:937110288807907378>":
                cur =  main.get_lang(ctx.guild, "CONFIG_CURRENCY").format(base.guild(ctx.guild)[4])
            else:
                cur = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[currency]`'  
            if base.guild(ctx.guild)[10] != 3:
                warnl = main.get_lang(ctx.guild, "CONFIG_WARNCOUNT").format(base.guild(ctx.guild)[10])               
            else: 
                warnl = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[warn]`'    
            if base.guild(ctx.guild)[11] != "mute":
                if base.guild(ctx.guild)[11] == "mute":
                    nakaztitle = f'{main.get_lang(ctx.guild, "CONFIG_MUTE")}'
                elif base.guild(ctx.guild)[11] == "kick":
                    nakaztitle = f'{main.get_lang(ctx.guild, "CONFIG_KICK")}'
                elif base.guild(ctx.guild)[11] == "ban":
                    nakaztitle = f'{main.get_lang(ctx.guild, "CONFIG_BAN")}'
                nakaz = main.get_lang(ctx.guild, "CONFIG_WARNPUN").format(nakaztitle)
            else:           
                nakaz = f'{main.get_lang(ctx.guild, "CONFIG_NOSET")} `[warnpun]`'
            
            emb = discord.Embed(description = f'{main.get_lang(ctx.guild, "CONFIG_TITLE")} \n\n {prefix} \n {lang} \n {autorole} \n {welcome} \n {goodbuy} \n {logs} \n {lvl} \n {cur} \n {warnl} \n {nakaz}', color = 0xFFA500)
            emb.set_footer(text = main.get_lang(ctx.guild, "CONFIG_FOOTER").format(ctx.prefix))
            view=DropdownView(ctx.guild)
            await ctx.send(embed=emb, view=view)

    @commands.Cog.listener()
    async def on_dropdown(self, inter:discord.MessageInteraction):
        prefix = cursor.execute("SELECT prefix FROM guilds WHERE guild = {}".format(inter.guild.id)).fetchone()[0]
        color = 0xff4444
        embed = discord.Embed(title = main.get_lang(inter.guild, "CONFIG1_TITLE"), description = main.get_lang(inter.guild, "CONFIG1_DESC").format(prefix), color = 0xFFA500)
        embed1 = discord.Embed(title = main.get_lang(inter.guild, "CONFIG2_TITLE"), description = main.get_lang(inter.guild, "CONFIG2_DESC").format(prefix), color = 0xFFA500)
        embed2 = discord.Embed(title = main.get_lang(inter.guild, "CONFIG3_TITLE"), description = main.get_lang(inter.guild, "CONFIG3_DESC").format(prefix), color = 0xFFA500)
        embed3 = discord.Embed(title = main.get_lang(inter.guild, "CONFIG4_TITLE"), description = main.get_lang(inter.guild, "CONFIG4_DESC").format(prefix), color = 0xFFA500)
        embed4 = discord.Embed(title = main.get_lang(inter.guild, "CONFIG5_TITLE"), description = main.get_lang(inter.guild, "CONFIG5_DESC").format(prefix), color = 0xFFA500)
        embed5 = discord.Embed(title = main.get_lang(inter.guild, "CONFIG6_TITLE"), description = main.get_lang(inter.guild, "CONFIG6_DESC").format(prefix), color = 0xFFA500)
        embed6 = discord.Embed(title = main.get_lang(inter.guild, "CONFIG7_TITLE"), description = main.get_lang(inter.guild, "CONFIG7_DESC").format(prefix), color = 0xFFA500)
        embed7 = discord.Embed(title = main.get_lang(inter.guild, "CONFIG8_TITLE"), description = main.get_lang(inter.guild, "CONFIG8_DESC").format(prefix), color = 0xFFA500)
        embed8 = discord.Embed(title = main.get_lang(inter.guild, "CONFIG9_TITLE"), description = main.get_lang(inter.guild, "CONFIG9_DESC").format(prefix), color = 0xFFA500)
        embed9 = discord.Embed(title = main.get_lang(inter.guild, "CONFIG10_TITLE"), description = main.get_lang(inter.guild, "CONFIG10_DESC").format(prefix), color = 0xFFA500)

        if inter.values[0] == '1':
            await inter.send(embed=embed, ephemeral=True)
        if inter.values[0] == '2':
            await inter.send(embed=embed1, ephemeral=True)
        if inter.values[0] == '3':
            await inter.send(embed=embed2, ephemeral=True)    
        if inter.values[0] == '4':
            await inter.send(embed=embed3, ephemeral=True) 
        if inter.values[0] == '5':
            await inter.send(embed=embed4, ephemeral=True)        
        if inter.values[0] == '6':
            await inter.send(embed=embed5, ephemeral=True)  
        if inter.values[0] == '7':
            await inter.send(embed=embed6, ephemeral=True) 
        if inter.values[0] == '8':
            await inter.send(embed=embed7, ephemeral=True)
        if inter.values[0] == '9':
            await inter.send(embed=embed8, ephemeral=True)               
        if inter.values[0] == '10':
            await inter.send(embed=embed9, ephemeral=True)                   

    @config.command(aliases=['префикс', 'pref', 'pr', 'преф', 'пр', 'Префикс', 'Prefix', 'Преф', 'Pref'])
    @commands.has_permissions(administrator = True)
    @block.block()
    async def prefix(self, ctx, prefix):
        base.send(f"UPDATE guilds SET prefix = '{prefix}' WHERE guild = '{ctx.guild.id}'")
        await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_PREFIX_UPDATE").format(ctx.author.mention, prefix), color = 0xFFA500))

        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_PREFIX_UPDATE").format(ctx.author.mention, prefix), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)
 
    @config.command()
    @commands.has_permissions(administrator = True)
    @block.block()
    async def currency(self, ctx, emoji):
        if emoji.startswith('<:') and emoji.endswith('>'):    
            base.send(f"UPDATE guilds SET currency = '{emoji}' WHERE guild = '{ctx.guild.id}'")
            await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_CURRENCY_UPDATE").format(ctx.author.mention, emoji), color = 0xFFA500))           
        else:            
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "CONFIG_CURRENCY_ERROR")))
            return   
        
        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_CURRENCY_UPDATE").format(ctx.author.mention, emoji), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)                       
            
    @config.command(aliases=['уровень', 'level', 'levelling', 'лвл', 'левел', 'уровни'])
    @commands.has_permissions(administrator = True)
    @block.block()
    async def lvl(self, ctx, channel: discord.TextChannel = None):
        if not channel:
            base.send(f"UPDATE guilds SET lvlmessage = NULL WHERE guild = '{ctx.guild.id}'")
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "CONFIG_RESET")))
            return

        base.send(f"UPDATE guilds SET lvlmessage = '{channel.id}' WHERE guild = '{ctx.guild.id}'")
        await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_LVL_UPDATE").format(ctx.author.mention, channel.mention), color = 0xFFA500))

        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_LVL_UPDATE").format(ctx.author.mention, channel.mention), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)
            

    @config.command(aliases=['приветствие', 'hello', 'hellochannel', 'hi', 'привет', 'welcoming', 'welcomee', 'welcom', 'велком', 'приветсовать'])
    @commands.has_permissions(administrator = True)
    @block.block()
    async def welcome(self, ctx, channel: discord.TextChannel = None):
        if not channel:
            base.send(f"UPDATE guilds SET welcome = NULL WHERE guild = '{ctx.guild.id}'")
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "CONFIG_RESET")))
            return

        base.send(f"UPDATE guilds SET welcome = '{channel.id}' WHERE guild = '{ctx.guild.id}'")
        await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_WELCOME_UPDATE").format(ctx.author.mention, channel.mention), color = 0xFFA500))

        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_WELCOME_UPDATE").format(ctx.author.mention, channel.mention), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)

    @config.command(aliases=['bye', 'byebye', 'прощание', 'прощатся', 'пока', 'поки', 'гудбай', 'bb', 'gb'])
    @commands.has_permissions(administrator = True)
    @block.block()
    async def goodbye(self, ctx, channel: discord.TextChannel = None):
        if not channel:
            base.send(f"UPDATE guilds SET goodbye = NULL WHERE guild = '{ctx.guild.id}'")
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "CONFIG_RESET")))
            return

        base.send(f"UPDATE guilds SET goodbye = '{channel.id}' WHERE guild = '{ctx.guild.id}'")
        await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_GOODBYE_UPDATE").format(ctx.author.mention, channel.mention), color = 0xFFA500))

        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_GOODBYE_UPDATE").format(ctx.author.mention, channel.mention), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)

    @config.command()
    @commands.has_permissions(administrator = True)
    @block.block()
    async def autorole(self, ctx, role: discord.Role = None):
        if not role:
            base.send(f"UPDATE guilds SET autorole = NULL WHERE guild = '{ctx.guild.id}'")
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "CONFIG_RESET")))
            return

        base.send(f"UPDATE guilds SET autorole = '{role.id}' WHERE guild = '{ctx.guild.id}'")
        await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_ROLE_UPDATE").format(ctx.author.mention, role.mention), color = 0xFFA500))

        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_ROLE_UPDATE").format(ctx.author.mention, role.mention), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)

    @config.command()
    @commands.has_permissions(administrator = True)
    @block.block()
    async def lang(self, ctx, *, langs = None):
        if langs == None:
            base.send(f"UPDATE guilds SET language = '{lang}' WHERE guild = '{ctx.guild.id}'")
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "CONFIG_RESET")))
            return
        else:
            if langs == "ru" or langs == "en" or langs == "ua":
                base.send(f"UPDATE guilds SET language = '{langs}' WHERE guild = '{ctx.guild.id}'")
                await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_LANG_UPDATE").format(ctx.author.mention, langs), color = 0xFFA500))
            else:
                print(f"{ctx.guild.name} ({ctx.guild.id}) пытается установить язык которого не существует")

        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_LANG_UPDATE").format(ctx.author.mention, channel.mention), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)

    @config.command(aliases=['логи', 'действия', 'лог', 'логирование', 'log', 'logging', 'actions'])
    @commands.has_permissions(administrator = True)
    @block.block()
    #@premium.premium()
    async def logs(self, ctx, channel: discord.TextChannel = None):
        if not channel:
            base.send(f"UPDATE guilds SET modlogs = NULL WHERE guild = '{ctx.guild.id}'")
            await ctx.reply(embed = main.done(ctx.guild, main.get_lang(ctx.guild, "CONFIG_RESET")))
            return

        base.send(f"UPDATE guilds SET modlogs = '{channel.id}' WHERE guild = '{ctx.guild.id}'")
        await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_LOGS_UPDATE").format(ctx.author.mention, channel.mention), color = 0xFFA500))

        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_LOGS_UPDATE").format(ctx.author.mention, channel.mention), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)

    @config.command(aliases=['варн', 'колво-варнов', 'варны', 'warns', 'warncount', 'warn-count'])
    @commands.has_permissions(administrator = True)
    @block.block()
    async def warn(self, ctx, count):
        base.send(f"UPDATE guilds SET warn = '{count}' WHERE guild = '{ctx.guild.id}'")
        await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_WARN_UPDATE").format(ctx.author.mention, count), color = 0xFFA500))
        #else:
        #    await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "ECONOMY_BANK_ZERO")))

        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_WARN_UPDATE").format(ctx.author.mention, count), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)

    @config.command(aliases=['наказание', 'punishment', 'warn-jail', 'наказ', 'наказать'])
    @commands.has_permissions(administrator = True)
    @block.block()
    async def warnpun(self, ctx, type):
        if type == "mute" or type == "kick" or type == "ban" or type == "мут" or type == "кик" or type == "бан" or type == "замутить" or type == "кикнуть" or type == "забанить":
            base.send(f"UPDATE guilds SET _warn = '{type}' WHERE guild = '{ctx.guild.id}'")
            await ctx.reply(embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_WARNPUN_UPDATE").format(ctx.author.mention, type), color = 0xFFA500))
        else:
            await ctx.reply(embed = main.deny(ctx.guild, main.get_lang(ctx.guild, "CONFIG_WARNPUN_ERROR")))

        if base.guild(ctx.guild)[6] is not None:

            embed = discord.Embed(description = main.get_lang(ctx.guild, "CONFIG_WARNPUN_UPDATE").format(ctx.author.mention, type), color = 0xFFA500, timestamp = datetime.utcnow())
            embed.set_footer(text = main.get_lang(ctx.guild, "MEMBER_ID").format(ctx.author.id))

            await self.client.get_channel(int(base.guild(ctx.guild)[6])).send(embed = embed)            

def setup(client):
    client.add_cog(Config(client))