#discord stuff
import discord
from discord.ext import commands
#dotenv stuff
import os
from dotenv import load_dotenv
#chatgpt stuff
import openai



load_dotenv()
TOKEN = os.getenv('TOKEN')
openai.organization = os.getenv('ORG_ID')
openai.api_key = os.getenv('API_KEY')
openai.Model.list()

bot = commands.Bot(command_prefix="~", intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("online")
@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")
@bot.command()
async def pong(ctx):
    await ctx.channel.send("ping")


@bot.command()
async def image(ctx, input):
    response = openai.Image.create(
        prompt = input,
        n = 1,
        size = '512x512'
    )
    image_url = response['data'][0]['url']
    await ctx.send(image_url)






bot.run(TOKEN)