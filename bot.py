import discord
import config
import slash_commands
import random
import asyncio
from discord.ext import commands
from discord import app_commands



intents = discord.Intents.default()
intents.message_content = True

bot=commands.Bot(command_prefix="!", intents=intents)
TOKEN = config.DISCORD_TOKEN

    
@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error:{e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    print(f"{username} said: '{user_message}' ({channel})")
    await bot.process_commands(message)



@bot.tree.command(name="hello")
async def hello(interaction:discord.Interaction):
   await slash_commands.hello(interaction)


@bot.tree.command(name="help")
async def help(interaction:discord.Interaction):
   await slash_commands.help(interaction)

@bot.tree.command(name="weather")
@app_commands.describe(location="Which place are you seraching for?")
async def weather(interaction:discord.Interaction,location:str):
    await slash_commands.weather(interaction,location)


@bot.tree.command(name="movie")
@app_commands.describe(movie_to_search="Which movie are you looking for?")
async def movie(interaction:discord.Interaction,movie_to_search:str):
    await slash_commands.movie(interaction,movie_to_search)


@bot.tree.command(name="poll")
@app_commands.describe(heading="What are we voting for?")
@app_commands.describe(options="Options for the poll.(e.g., oprion1, option2, option3)")
async def poll(interaction: discord.Interaction,heading:str ,options: str):
   await slash_commands.poll(interaction, heading,options)


@bot.tree.command(name="who_is_right")
@app_commands.describe(timeout="seconds to start")
async def who_is_right(interaction: discord.Interaction, timeout: int):
   await slash_commands.who_is_right(interaction=interaction,timeout=timeout)


@bot.tree.command(name="send_image")
async def send_image(interaction:discord.Interaction):
    await slash_commands.send_image(interaction=interaction)

@bot.tree.command(name="meme_ege")
@app_commands.describe(text="the text you want to put on the meme")
async def meme_ege(interaction:discord.Interaction,text:str):
    await slash_commands.meme_generator(interaction=interaction,text=text,y_position=20,name="ege")


@bot.tree.command(name="meme_isil")
@app_commands.describe(text="the text you want to put on the meme")
async def meme_isil(interaction:discord.Interaction,text:str):
    await slash_commands.meme_generator(interaction=interaction,text=text,y_position=700,name="isil")


@bot.tree.command(name="meme_ozge")
@app_commands.describe(text="the text you want to put on the meme")
async def meme_ozge(interaction:discord.Interaction,text:str):
    await slash_commands.meme_generator(interaction=interaction,text=text,y_position=1200,name="ozge")

host_site="www.google.com"
@bot.tree.command(name="ping")
async def ping(interaction:discord.Interaction):
    await slash_commands.ping(host_site,interaction=interaction)


    
"""
@bot.tree.command(name="gpt")
@app_commands.describe(chat="Your message to chatGPT")
async def gpt_command(interaction: discord.Interaction,chat:str):
    await slash_commands.gpt_command(interaction,chat)



@bot.tree.command(name="youtube")
@app_commands.describe(url="Type video url")
async def youtube_play(interaction:discord.Interaction, url:str):
    await youtube_player.play_youtube(interaction,url)


    """


bot.run(TOKEN)