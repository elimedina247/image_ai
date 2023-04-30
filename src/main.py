#discord stuff
import discord
from discord.ext import commands
#dotenv stuff
import os
from dotenv import load_dotenv
#chatgpt stuff
import openai
#DeepAPI stuff
import requests





load_dotenv()
TOKEN = os.getenv('TOKEN')#Discord bot token
openai.organization = os.getenv('ORG_ID')#chatGPT org ID
openai.api_key = os.getenv('API_KEY_GPT')#ChatGPT API
openai.Model.list()

DEEPAI_API = os.getenv('API_KEY_DEEP')#DeepAI

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


# @bot.command()
# async def image(ctx, *input):
#     str = ' '.join(input)
#     input = ''.join(input)
#     response = openai.Image.create(
#         prompt = input,
#         n = 1,
#         size = '512x512'
#     )
#     image_url = response['data'][0]['url']
#     await ctx.send("Here is: " + str)
#     await ctx.send(image_url)


@bot.command()
async def gpt(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = openai.Image.create(
            prompt = input,
            n = 1,
            size = '512x512'
        )
        image_url = response['data'][0]['url']
        await ctx.send("Here is: " + str)
        await ctx.send(image_url)
    except openai.error.InvalidRequestError:
        await ctx.send(str + " has been rejected by ChatGPT safety system.Try ~deep '" + str + "' command instead.")


@bot.command()
async def large_gpt(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = openai.Image.create(
            prompt = input,
            n = 1,
            size = '1024x1024'
        )
        image_url = response['data'][0]['url']
        await ctx.send("Here is: " + str)
        await ctx.send(image_url)
    except openai.error.InvalidRequestError:
        await ctx.send(str + " has been rejected by ChatGPT safety system. Try ~deep '" + str + "' command instead")
    except openai.error.RateLimitError:
        await ctx.send("ChatGPT rate limit exceeded. Slow ur roll ")






@bot.command()
async def deep(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = requests.post(
            "https://api.deepai.org/api/text2img",
            data={
                'text': input,
                'grid_size': "1"
            },
            headers={'api-key': '91066d5a-5d7d-415d-82a0-b607493081c3'}
        )
        await ctx.send("Here is: " + str)
        await ctx.send(response.json()['output_url'])

    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send("Error idk why this API doesn't tell me shit.")
    #print(response.json())

@bot.command()
async def deep_3d(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = requests.post(
            "https://api.deepai.org/api/3d-character-generator",
            data={
                'text': input,
                'grid_size': "1"
            },
            headers={'api-key': '91066d5a-5d7d-415d-82a0-b607493081c3'}
        )
        await ctx.send("Here is 3d character: " + str)
        await ctx.send(response.json()['output_url'])

    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send("Error idk why this API doesn't tell me shit.")
    #print(response.json())

@bot.command()
async def deep_fantasy(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = requests.post(
            "https://api.deepai.org/api/fantasy-character-generator",
            data={
                'text': input,
                'grid_size': "1"
            },
            headers={'api-key': '91066d5a-5d7d-415d-82a0-b607493081c3'}

        )
        #print(response.json())
        await ctx.send("Here is fantasy: " + str)
        await ctx.send(response.json()['output_url'])

    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send("Error idk why this API doesn't tell me shit.")


@bot.command()
async def deep_pixel(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = requests.post(
            "https://api.deepai.org/api/pixel-art-generator",
            data={
                'text': input,
                'grid_size': "1"
            },
            headers={'api-key': '91066d5a-5d7d-415d-82a0-b607493081c3'}
        )
        await ctx.send("Here is pixel: " + str)
        await ctx.send(response.json()['output_url'])

    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send("Error idk why this API doesn't tell me shit.")


@bot.command()
async def deep_origami(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = requests.post(
            "https://api.deepai.org/api/origami-3d-generator",
            data={
                'text': input,
                'grid_size': "1"
            },
            headers={'api-key': '91066d5a-5d7d-415d-82a0-b607493081c3'}
        )
        await ctx.send("Here is origami: " + str)
        await ctx.send(response.json()['output_url'])

    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send("Error idk why this API doesn't tell me shit.")




@bot.command()
async def deep_surreal(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = requests.post(
            "https://api.deepai.org/api/surreal-graphics-generator",
            data={
                'text': input,
                'grid_size': "1"
            },
            headers={'api-key': '91066d5a-5d7d-415d-82a0-b607493081c3'}
        )
        await ctx.send("Here is surreal: " + str)
        await ctx.send(response.json()['output_url'])

    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send("Error idk why this API doesn't tell me shit.")




@bot.command()
async def deep_impressionism(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = requests.post(
            "https://api.deepai.org/api/impressionism-painting-generator",
            data={
                'text': input,
                'grid_size': "1"
            },
            headers={'api-key': '91066d5a-5d7d-415d-82a0-b607493081c3'}
        )
        await ctx.send("Here is impressionism: " + str)
        await ctx.send(response.json()['output_url'])

    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send("Error idk why this API doesn't tell me shit.")





@bot.command()
async def deep_abstract(ctx, *input):
    str = ' '.join(input)
    input = ''.join(input)
    try:
        response = requests.post(
            "https://api.deepai.org/api/abstract-painting-generator",
            data={
                'text': input,
                'grid_size': "1"
            },
            headers={'api-key': '91066d5a-5d7d-415d-82a0-b607493081c3'}
        )
        await ctx.send("Here is abstract: " + str)
        await ctx.send(response.json()['output_url'])

    except discord.ext.commands.errors.CommandInvokeError:
        await ctx.send("Error idk why this API doesn't tell me shit.")



@bot.command()
async def commands(ctx):
    await ctx.send("Ping\n"
                   "Pong\n"
                   "large_gpt: ChatGPT 1024x1024 image\n"
                   "gpt: ChatGPT 512x512 image\n"
                   "deep: Deep AI image\n"
                   "deep_3d: Deep AI 3d character generator\n"
                   "deep_fantasy: Deep AI fantasy generator\n"
                   "deep_pixel: Deep AI pixel\n"
                   "deep_origami: Deep AI 3d origami\n"
                   "deep_surreal: Deep AI surreal\n"
                   "deep_abstract: Deep AI abstract\n"
                   "deep_impressionism: Deep AI Impressionism\n"
                   )

bot.run(TOKEN)