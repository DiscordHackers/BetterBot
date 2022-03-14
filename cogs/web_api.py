from xmlrpc.client import Boolean
from disnake import *
from disnake.ext import commands
import random
from flask import Flask, jsonify, url_for, redirect, request, send_file, render_template, send_from_directory
from werkzeug.exceptions import HTTPException
import json
from threading import Thread
from functools import partial
from PIL import Image, ImageFilter, ImageOps, ImageEnhance
from PIL.ImageFilter import BLUR
import requests
import io
from petpetgif import petpet as petpetgif
from api.check import utils, block, support

versionapi = 'v2'

def html(content):  # Also allows you to set your own <head></head> etc
   return '<html><head>BetterBot API [v2] <br /> Thanks for frimebot.ru <br /><br /></head><body>' + content + '</body><style>a{text-decoration:None;color:black;}a:hover{color:blue;}</style></html>'

versionapi_url = f'/{versionapi}/'

def web_status():
    with open("./utils/web_config.json") as f:
        config = json.load(f)
    return Boolean(config['STATUS'])

def get_key():
    with open("./utils/web_config.json") as f:
        config = json.load(f)
    return str(config['KEY'])

def get_auth_status():
    with open("./utils/web_config.json") as f:
        config = json.load(f)
    return Boolean(config['USE_KEY'])

class APIException(Exception):

    def __init__(self, message=None, status_code=406):
        if message == None:
            super().__init__('The API is currently unavailable!')
            self.status_code = status_code
            return
        super().__init__(message)
        self.status_code = status_code

class WebApiCog(commands.Cog, name="Web Api Cog"):
    

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['SERVER_NAME'] = '172.18.0.5'
    app.config['SERVER_NAME'] = '172.18.0.5:1343'
    
    @app.route(versionapi_url + 'facts')
    def api_facts():
        if not web_status(): raise APIException()
        data = request.values
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        facts = json.load(open('./utils/data/facts.json', encoding='utf-8'))
        fact = random.choice(facts)
        return jsonify({"fact":f"{fact}"})

    
    @app.route(versionapi_url + 'picture/dog')
    def api_image_dog():
        if not web_status(): raise APIException()
        data = request.values
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        dogs = json.load(open('./utils/data/dog_images.json', encoding='utf-8'))
        dog = random.choice(dogs)
        return jsonify({"image":f"{dog}"})


    @app.route(versionapi_url + 'picture/cat')
    def api_image_cat():
        if not web_status(): raise APIException()
        data = request.values
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        cats = json.load(open('./utils/data/cat_images.json', encoding='utf-8'))
        cat = random.choice(cats)
        return jsonify({"image":f"{cat}"})


    @app.route(versionapi_url + 'roleplay/hug')
    def api_gif_hug():
        if not web_status(): raise APIException()
        data = request.values
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        hug_ = json.load(open('./utils/data/hug_gif.json', encoding='utf-8'))
        hug = random.choice(hug_)
        return jsonify({"image":f"{hug}"})


    @app.route(versionapi_url + 'roleplay/slap')
    def api_gif_slap():
        if not web_status(): raise APIException()
        data = request.values
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        slap_ = json.load(open('./utils/data/slap_gif.json', encoding='utf-8'))
        slap = random.choice(slap_)
        return jsonify({"image":f"{slap}"})


    @app.route(versionapi_url + 'roleplay/kiss')
    def api_gif_kiss():
        if not web_status(): raise APIException()
        data = request.values
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        kiss_ = json.load(open('./utils/data/kiss_gif.json', encoding='utf-8'))
        kiss = random.choice(kiss_)
        return jsonify({"image":f"{kiss}"})

    @app.route('/')
    def not_home():
        if not web_status(): raise APIException()
        data = request.values
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        return redirect(f'https://api.betterbot.ru{versionapi_url}')


    @app.route(versionapi_url + 'filter/blur')
    def filter_blur():
        data = request.values
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        try: image_url = data['avatar']
        except: raise APIException("Missing avatar queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw)
        file_object = io.BytesIO()
        img1 = img_.filter(BLUR)
        img2 = img1.filter(BLUR)
        img  = img2.filter(ImageFilter.MinFilter(size=3))
        img.save(file_object, 'PNG')
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')

    @app.route(versionapi_url + 'filter/grayscale')
    def filter_grayscale():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw)
        img = ImageOps.grayscale(img_)
        file_object = io.BytesIO()
        img.save(file_object, 'PNG')
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')


    @app.route(versionapi_url + 'filter/invert')
    def filter_invert():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw)
        file_object = io.BytesIO()
        img = ImageOps.invert(img_)
        img.save(file_object, 'PNG')
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')


    @app.route(versionapi_url + 'filter/wasted')
    def filter_wasted():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw) # Аватар
        img_ = img_.resize((500,500))
        img = ImageOps.grayscale(img_)
        img2 = Image.open('./utils/images/wasted_template.png')
        img = img.convert('RGB')
        img.paste(img2, (0,0), img2)
        file_object = io.BytesIO()
        img.save(file_object, format="png")
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')


    @app.route(versionapi_url + 'filter/glass')
    def filter_glass():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw) # Аватар
        img_ = img_.resize((500,500))
        img = ImageOps.grayscale(img_)
        img2 = Image.open('./utils/images/glass_template.png')
        img = img.convert('RGB')
        img.paste(img2, (0,0), img2)
        file_object = io.BytesIO()
        img.save(file_object, format="png")
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')


    @app.route(versionapi_url + 'filter/gay')
    def filter_gay():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw) # Аватар
        img_ = img_.resize((500,500))
        img = ImageOps.grayscale(img_)
        img2 = Image.open('./utils/images/rainbow_template.png')
        img = img.convert('RGB')
        img.paste(img2, (0,0), img2)
        file_object = io.BytesIO()
        img.save(file_object, format="png")
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')


    @app.route(versionapi_url + 'filter/jail')
    def filter_jail():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw) # Аватар
        img_ = img_.resize((512,512))
        img = ImageOps.grayscale(img_)
        img2 = Image.open('./utils/images/jail_template.png')
        img = img.convert('RGB')
        img.paste(img2, (0,0), img2)
        file_object = io.BytesIO()
        img.save(file_object, format="png")
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')


    @app.route(versionapi_url + 'filter/petpet')
    def gif_petpet():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img = r.raw
        file_object = io.BytesIO()
        petpetgif.make(img, file_object)
        file_object.seek(0)
        return send_file(file_object, mimetype='image/GIF')


    @app.route(versionapi_url + 'filter/comrade')
    def filter_comrade():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw) # Аватар
        img_ = img_.resize((512,512))
        img = ImageOps.grayscale(img_)
        img2 = Image.open('./utils/images/comrade_template.png')
        img = img.convert('RGB')
        img.paste(img2, (0,0), img2)
        file_object = io.BytesIO()
        img.save(file_object, format="png")
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')
    
    @app.route(versionapi_url + 'filter/passed')
    def filter_passed():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw) # Аватар
        img = img_.resize((512,512))
        img2 = Image.open('./utils/images/passed_template.png')
        img.paste(img2, (0,0), img2)
        file_object = io.BytesIO()
        img.save(file_object, format="png")
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')

    @app.route(versionapi_url + 'filter/brightness')
    def filter_bright():
        data = request.values
        try:
            image_url = data['avatar']
        except:
            raise APIException("Missing avatar queries")
        if get_auth_status():
            try:
                if data['key'] != get_key(): raise APIException("Invalid key")
            except: raise APIException("Missing key queries")
        r = requests.get(image_url, stream=True)
        img_ = Image.open(r.raw) # Аватар
        img = img_.resize((512,512))
        factor = 1.5
        enhancer = ImageEnhance.Brightness(img)
        imgoutput = enhancer.enhance(factor)
        file_object = io.BytesIO()
        imgoutput.save(file_object, format="png")
        file_object.seek(0)
        return send_file(file_object, mimetype='image/PNG')

    @app.errorhandler(Exception)
    def handle_error(e):
        code = 500
        if isinstance(e, HTTPException):
            code = e.code
        return jsonify(error=str(e)), code


    @app.route(versionapi_url)
    def home():
        if not web_status(): raise APIException()
        return render_template("home.html")

    @app.route(versionapi_url + "roleplay")
    def homee():
        if not web_status(): raise APIException()
        return render_template("roleplay.html")   

    @app.route(versionapi_url + "filter")
    def homeee():
        if not web_status(): raise APIException()
        return render_template("filter.html") 

    @app.route(versionapi_url + "picture")
    def homeeee():
        if not web_status(): raise APIException()
        return render_template("picture.html")                          
        
    @commands.group()
    async def web(self ,ctx, param=None, new='off'):
        if param==None:
            await ctx.reply("Укажите нужный аргумент! **`status`**, **`auth`**")
            return
        if (param != 'auth') and (param != 'status'):
            await ctx.reply("Укажите нужный аргумент! **`status`**, **`auth`**")
            return
        if param == 'auth':
            if (new != 'off') and (new != 'on'):
                await ctx.reply("Ошибка аргументов! Доступны: **`on`**/**`off`**")
                return
            if new == 'off': status = False
            else: status = True
            with open("./utils/web_config.json") as f:
                config = json.load(f)
            config['USE_KEY'] = status
            with open("./utils/web_config.json", "w") as f:
                json.dump(config, f)
            await ctx.reply(f'Статус AUTH WEB API теперь: **{new}**'.replace('on', '`🟢`').replace('off', '`🔴`'))
        else:
            if (new != 'off') and (new != 'on'):
                await ctx.reply("Ошибка аргументов! Доступны: **`on`**/**`off`**")
                return
            if new == 'off': status = False
            else: status = True
            with open("./utils/web_config.json") as f:
                config = json.load(f)
            config['STATUS'] = status
            with open("./utils/web_config.json", "w") as f:
                json.dump(config, f)
            await ctx.reply(f'Статус WEB API теперь: **{new}**'.replace('on', '`🟢`').replace('off', '`🔴`'))


    #@commands.Cog.listener()
    #async def on_command_error(self,ctx,error):
        #await ctx.reply(f'```{error}```')

    @commands.Cog.listener()
    async def on_ready(self):
        print('ptero start')
        partial_run = partial(self.app.run, host="0.0.0.0", port=1343, use_reloader=False, debug=True)
        t = Thread(target=partial_run)
        t.setDaemon(True)
        t.start()

def setup(bot: commands.Bot):
    bot.add_cog(WebApiCog(bot))