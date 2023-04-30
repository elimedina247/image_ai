#discord stuff
import discord
from discord.ext import commands
#dotenv stuff
import os
from dotenv import load_dotenv
#chatgpt stuff

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")


bot.run(TOKEN)