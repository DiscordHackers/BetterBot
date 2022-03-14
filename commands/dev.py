import disnake as discord
from disnake.ext import commands
from api.check import utils, block
from api.server import base, main
import datetime

class Dev(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @utils.developer()
    async def badge(self, ctx, member: discord.Member, option, value):
        if option == "dev" or option == "developer" or option == "разраб" or option == "дев" or option == "разработчик":
            if value == "1" or value == "0":
                base.send(f"UPDATE bages SET dev = {value} WHERE userid = {member.id}")
                await ctx.reply(embed = main.done(ctx.guild, f"Вы успешно установили пользователю {member.mention} награду **Разработчик** на **{value}**"))
            else:
                await ctx.reply(embed = main.deny(ctx.guild, "Вы указали неправильное значение \n\n Доступные значения: \n > **1** или **0**"))
        if option == "moder" or option == "mod" or option == "moderator" or option == "мод" or option == "модер" or option == "модератор":
            if value == "1" or value == "0":
                base.send(f"UPDATE bages SET moder = {value} WHERE userid = {member.id}")
                await ctx.reply(embed = main.done(ctx.guild, f"Вы успешно установили пользователю {member.mention} награду **Модератор** на **{value}**"))
            else:
                await ctx.reply(embed = main.deny(ctx.guild, "Вы указали неправильное значение \n\n Доступные значения: \n > **1** или **0**"))      
        if option == "bug" or option == "баг" or option == "буг" or option == "багхантер":                      
            if value == "1" or value == "0":
                base.send(f"UPDATE bages SET bughunt = {value} WHERE userid = {member.id}")
                await ctx.reply(embed = main.done(ctx.guild, f"Вы успешно установили пользователю {member.mention} награду **Охотник за багами** на **{value}**"))
            else:
                await ctx.reply(embed = main.deny(ctx.guild, "Вы указали неправильное значение \n\n Доступные значения: \n > **1** или **0**"))    
        if option == "idea" or option == "идея" or option == "head" or option == "голова":                      
            if value == "1" or value == "0":
                base.send(f"UPDATE bages SET idea = {value} WHERE userid = {member.id}")
                await ctx.reply(embed = main.done(ctx.guild, f"Вы успешно установили пользователю {member.mention} награду **Большая голова** на **{value}**"))
            else:
                await ctx.reply(embed = main.deny(ctx.guild, "Вы указали неправильное значение \n\n Доступные значения: \n > **1** или **0**"))   
        if option == "supporter" or option == "поддержавший" or option == "money" or option == "деньги" or option == "support" or option == "supported":                      
            if value == "1" or value == "0":
                base.send(f"UPDATE bages SET supported = {value} WHERE userid = {member.id}")
                await ctx.reply(embed = main.done(ctx.guild, f"Вы успешно установили пользователю {member.mention} награду **Поддержавший** на **{value}**"))
            else:
                await ctx.reply(embed = main.deny(ctx.guild, "Вы указали неправильное значение \n\n Доступные значения: \n > **1** или **0**"))   
        if option == "партнер" or option == "партнёр" or option == "part" or option == "partner":                      
            if value == "1" or value == "0":
                base.send(f"UPDATE bages SET partner = {value} WHERE userid = {member.id}")
                await ctx.reply(embed = main.done(ctx.guild, f"Вы успешно установили пользователю {member.mention} награду **Партнер** на **{value}**"))
            else:
                await ctx.reply(embed = main.deny(ctx.guild, "Вы указали неправильное значение \n\n Доступные значения: \n > **1** или **0**"))                     
        if option == "all":
            if value == "1" or value == "0":
                base.send(f"UPDATE bages SET partner = {value} WHERE userid = {member.id}")
                base.send(f"UPDATE bages SET supported = {value} WHERE userid = {member.id}")
                base.send(f"UPDATE bages SET idea = {value} WHERE userid = {member.id}")
                base.send(f"UPDATE bages SET bughunt = {value} WHERE userid = {member.id}")
                base.send(f"UPDATE bages SET moder = {value} WHERE userid = {member.id}")
                base.send(f"UPDATE bages SET dev = {value} WHERE userid = {member.id}")
                await ctx.reply(embed = main.done(ctx.guild, f"Вы успешно установили пользователю {member.mention} все награды на **{value}**"))
            else:
                await ctx.reply(embed = main.deny(ctx.guild, "Вы указали неправильное значение \n\n Доступные значения: \n > **1** или **0**"))                
                                     
def setup(client):
    client.add_cog(Dev(client))