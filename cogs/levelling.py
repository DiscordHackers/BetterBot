import disnake as discord
from disnake.ext import commands
from PIL import Image, ImageDraw, ImageFont
import aiosqlite
import sqlite3
import math
import random
import aiohttp
import calendar
import io
from datetime import datetime
from api.check import block
from api.server import base, main

class Levelling(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.db = None
        self.client.loop.create_task(self.connect_database())

    async def connect_database(self):
        self.db = await aiosqlite.connect('./data/db/main/Database.db')

    async def find_or_insert_user(self, member: discord.Member):
        # user_id, guild_id, xp, level
        cursor = await self.db.cursor()
        await cursor.execute('Select * from users where guild = ? and id = ?', (member.guild.id, member.id))
        result = await cursor.fetchone()
        return result

    def calculate_xp(self, level):
        return 100 * (level ** 2)

    def calculate_level(self, xp):
        # Sqrt => value ** 0.5
        return round(0.1 * math.sqrt(xp))


    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot is True or message.guild is None:
            return

        result = await self.find_or_insert_user(message.author)

        id, guild, xp, level = result[2], result[0], result[3], result[4]
        #print(id, guild, xp, level)

        xp += random.randint(10, 40)

        if self.calculate_level(xp) > level:
            level += 1
            # 1,000
            if base.guild(message.guild)[9] is not None:
                embed = discord.Embed(title = main.get_lang(message.guild, "LEVEL_MEMBER_GUILD_TITLE"), description = main.get_lang(message.guild, "LEVEL_MEMBER_GUILD_DESC").format(message.author.mention, level), timestamp = datetime.utcnow(), color = 0xead967)
                await self.client.get_channel(int(base.guild(message.guild)[9])).send(embed = embed)

        cursor = await self.db.cursor()
        await cursor.execute('Update users set xp=?, level=? where id=? and guild=?', (xp, level, id, guild))
        await self.db.commit()

    async def make_rank_image(self, member: discord.Member, rank, level, xp, final_xp):
        user_avatar_image = str(member.avatar.url)
        async with aiohttp.ClientSession() as session:
            async with session.get(user_avatar_image) as resp:
                avatar_bytes = io.BytesIO(await resp.read())

        img = Image.new('RGB', (1000, 240))
        logo = Image.open(avatar_bytes).resize((200, 200))

        # Stack overflow helps :)
        bigsize = (logo.size[0] * 3, logo.size[1] * 3)
        mask = Image.new('L', bigsize, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + bigsize, fill=255)
        mask = mask.resize(logo.size, Image.ANTIALIAS)
        logo.putalpha(mask)
        ##############################
        img.paste(logo, (20, 20), mask=logo)

        # Black Circle
        draw = ImageDraw.Draw(img, 'RGB')
        draw.ellipse((152, 152, 208, 208), fill='#000')

        # Placing offline or Online Status
        # Discord Colors (Online: '#43B581')
        t = member.status
        if t == discord.Status.online:
            draw.ellipse((155, 155, 205, 205), fill='#43B581')

        t = member.status
        if t == discord.Status.offline:
            draw.ellipse((155, 155, 205, 205), fill='#2F3136')
            draw.ellipse((155, 155, 205, 205), fill='#8D96A1')

        t = member.status
        if t == discord.Status.idle:
            draw.ellipse((155, 155, 205, 205), fill='#FAA61A')

        t = member.status
        if t == discord.Status.dnd:
            draw.ellipse((155, 155, 205, 205), fill='#F04747')
        ##################################

        # Working with fonts
        big_font = ImageFont.FreeTypeFont('data/fonts/NeutralFace.otf', 60)
        medium_font = ImageFont.FreeTypeFont('data/fonts/NeutralFace.otf', 40)
        small_font = ImageFont.FreeTypeFont('data/fonts/NeutralFace.otf', 30)
        vsmall_font = ImageFont.FreeTypeFont('data/fonts/NeutralFace.otf', 15)


        # Placing Level text (right-upper part)
        text_size = draw.textsize(f"{level}", font=big_font)
        offset_x = 1000-15 - text_size[0]
        offset_y = 5
        draw.text((offset_x, offset_y), f"{level}", font=big_font, fill="#3560fc")
        text_size = draw.textsize('LEVEL', font=small_font)

        offset_x -= 5 + text_size[0]
        offset_y = 35
        draw.text((offset_x, offset_y), "LEVEL", font=small_font, fill="#3560fc")

        # Placing Rank Text (right upper part)
        text_size = draw.textsize(f"#{rank}", font=big_font)
        offset_x -= 15 + text_size[0]
        offset_y = 8
        draw.text((offset_x, offset_y), f"#{rank}", font=big_font, fill="#fff")

        text_size = draw.textsize("RANK", font=small_font)
        offset_x -= 5 + text_size[0]
        offset_y = 35
        draw.text((offset_x, offset_y), "RANK", font=small_font, fill="#fff")

        # Placing Progress Bar
        # Background Bar
        bar_offset_x = logo.size[0] + 20 + 100
        bar_offset_y = 160
        bar_offset_x_1 = 1000 - 50
        bar_offset_y_1 = 200
        circle_size = bar_offset_y_1 - bar_offset_y

        # Progress bar rect greyier one
        draw.rectangle((bar_offset_x, bar_offset_y, bar_offset_x_1, bar_offset_y_1), fill="#727175")
        # Placing circle in progress bar

        # Left circle
        draw.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x + circle_size//2, bar_offset_y + circle_size), fill="#727175")

        # Right Circle
        draw.ellipse((bar_offset_x_1 - circle_size//2, bar_offset_y, bar_offset_x_1 + circle_size//2, bar_offset_y_1), fill="#727175")

        # Filling Progress Bar

        bar_length = bar_offset_x_1 - bar_offset_x
        # Calculating of length
        # Bar Percentage (final_xp - current_xp)/final_xp

        # Some variables
        progress = (final_xp - xp) * 100/final_xp
        progress = 100 - progress
        progress_bar_length = round(bar_length * progress/100)
        pbar_offset_x_1 = bar_offset_x + progress_bar_length

        # Drawing Rectangle
        draw.rectangle((bar_offset_x, bar_offset_y, pbar_offset_x_1, bar_offset_y_1), fill="#3560fc")
        # Left circle
        draw.ellipse((bar_offset_x - circle_size//2, bar_offset_y, bar_offset_x + circle_size//2, bar_offset_y + circle_size), fill="#3560fc")
        # Right Circle
        draw.ellipse((pbar_offset_x_1 - circle_size//2, bar_offset_y, pbar_offset_x_1 + circle_size//2, bar_offset_y_1), fill="#3560fc")


        def convert_int(integer):
            integer = round(integer / 1000, 2)
            return f'{integer}K'

        # Drawing Xp Text
        text = f"/ {convert_int(final_xp)} XP"
        xp_text_size = draw.textsize(text, font=small_font)
        xp_offset_x = bar_offset_x_1 - xp_text_size[0]
        xp_offset_y = bar_offset_y - xp_text_size[1] - 10
        draw.text((xp_offset_x, xp_offset_y), text, font=small_font, fill="#727175")

        text = f'{convert_int(xp)} '
        xp_text_size = draw.textsize(text, font=small_font)
        xp_offset_x -= xp_text_size[0]
        draw.text((xp_offset_x, xp_offset_y), text, font=small_font, fill="#fff")

        # Placing User Name
        text = member.display_name
        text_size = draw.textsize(text, font=vsmall_font)
        text_offset_x = bar_offset_x - 10
        text_offset_y = bar_offset_y - text_size[1] - 25
        draw.text((text_offset_x, text_offset_y), text, font=small_font, fill="#fff")

        # Placing Discriminator
        text = f'#{member.discriminator}'
        text_offset_x += text_size[0] + 145
        text_size = draw.textsize(text, font=small_font)
        text_offset_y = bar_offset_y - text_size[1] - 15
        draw.text((text_offset_x, text_offset_y), text, font=small_font, fill="#727175")

        bytes = io.BytesIO()
        img.save(bytes, 'PNG')
        bytes.seek(0)
        return bytes



    @commands.command()
    async def rank(self, ctx: commands.Context, member: discord.Member=None):
        member = member or ctx.author
        cursor = await self.db.cursor()
        user = await self.find_or_insert_user(member)
        id, guild, xp, level = user[2], user[0], user[3], user[4]
        await cursor.execute("Select Count(*) from users where xp > ? and guild=?", (xp, guild))
        result = await cursor.fetchone()
        rank = result[0] + 1
        final_xp = self.calculate_xp(level + 1)
        bytes = await self.make_rank_image(member, rank, level, xp, final_xp)
        file = discord.File(bytes, 'rank.png')
        await ctx.send(file=file)

    @commands.command(aliases=['ui', 'user', 'юзер', 'профиль', 'юзеринфо'])
    @block.block()
    async def userinfo(self, ctx, user: discord.Member = None):
        user = user or ctx.message.author
        guild = ctx.message.guild
        guild_owner = guild.owner
        avi = user.avatar
        roles = sorted(user.roles, key=lambda r: r.position)

        for role in roles:
            if str(role.color) != '#000000':
                color = role.color
        if 'color' not in locals():
            color = 0

        test = int(user.created_at.timestamp())
        test2 = int(user.joined_at.timestamp())

        t = user.status
        if t == discord.Status.online:
            d = f"{main.get_lang(ctx.guild, 'ONLINE')}"

        if t == discord.Status.offline:
            d = f"{main.get_lang(ctx.guild, 'OFFLINE')}"

        if t == discord.Status.idle:
            d = f"{main.get_lang(ctx.guild, 'IDLE')}"

        if t == discord.Status.dnd:
            d = f"{main.get_lang(ctx.guild, 'DND')}"

        rolenames = ', '.join([r.name for r in roles if r != '@everyone']) or 'None'
        time = ctx.message.created_at
        member_number = sorted(guild.members, key=lambda m: m.joined_at).index(user) + 1
        member = user or ctx.author
        cursor = await self.db.cursor()
        user1 = await self.find_or_insert_user(member)
        id, guild, xp, level = user1[2], user1[0], user1[3], user1[4]
        await cursor.execute("Select Count(*) from users where xp > ? and guild=?", (xp, guild))
        result = await cursor.fetchone()
        rank = result[0] + 1
        final_xp = self.calculate_xp(level + 1)
        em = discord.Embed(color=9579219, timestamp=time)
        em.set_author(name=f'{main.get_lang(ctx.guild, "UI_1").format(user.name)}', icon_url = None or user.avatar)
        em.add_field(name=f'{main.get_lang(ctx.guild, "UI_2")}', value=f'{main.get_lang(ctx.guild, "UI_3").format(user.name, d, test2, test)}', inline=False),
        em.add_field(name=f'{main.get_lang(ctx.guild, "UI_4")}', value=f'{level}', inline=True)
        em.add_field(name=f'{main.get_lang(ctx.guild, "UI_5")}', value=f'{xp}/{final_xp}', inline=True)
        em.set_thumbnail(url=avi or None)
        better_dev = self.client.get_emoji(931877067526660138)
        better_moder = self.client.get_emoji(931880929033617438)
        better_supported = self.client.get_emoji(931879275861250048)
        better_partner = self.client.get_emoji(931881957590200320)
        better_bughunt = self.client.get_emoji(931878698645340201)

        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Levelling(client))