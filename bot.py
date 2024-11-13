import discord
import bot_logic
import gen_pass
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("HIIII!")

@bot.command()
async def bye(ctx):
    await ctx.send("GOOD BYEE :D!")

@bot.command()
async def SIX(ctx):
    await ctx.send("")

@bot.command()
async def portu(ctx):
    await ctx.send("voce ñao fala portugues e eu sim")

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass(10))

@bot.command()
async def mem(ctx):
    with open('imagenes/mem1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def mem1(ctx):
    with open('imagenes/mem2.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('imagenes/mem4.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def ramen(ctx):
    imagenes = os.listdir('imagenes')
    with open(f'imagenes/{random.choice(imagenes)}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):

        await ctx.send("Tienes que darme un pokemon")

bot.run('')
