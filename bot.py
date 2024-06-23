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
interaction_states = {}  # Dictionary to track interaction states for each user
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

"""
@bot.tree.command(name="meme_name")
@app_commands.describe(text="the text you want to put on the meme")
async def meme_ege(interaction:discord.Interaction,text:str):
    await slash_commands.meme_generator(interaction=interaction,text=text,y_position=20,name="name")
"""

host_site="www.google.com"
@bot.tree.command(name="ping")
async def ping(interaction:discord.Interaction):
    await slash_commands.ping(host_site,interaction=interaction)


@bot.tree.command(name="watch_tracker")
async def watch_tracker(interaction: discord.Interaction):
    user_id = str(interaction.user.id)
    
    # Check if the user already has an ongoing interaction
    if user_id in interaction_states and interaction_states[user_id] == 'ongoing':
        await interaction.response.send_message("You already have an ongoing action. Please complete it before starting a new one.", ephemeral=True)
        return
    
    interaction_states[user_id] = 'ongoing'  # Set state to ongoing
    embed = discord.Embed(
        title="Watch Tracker",
        description="Select an action by typing the corresponding number:\n1. Add a new entry\n2. Update an existing entry\n3. Remove an entry\n4. View watchlist\n5. Cancel",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed, ephemeral=True)
    
    def check(msg):
        return msg.author == interaction.user and msg.channel == interaction.channel and msg.content.isdigit()
    
    try:
        msg = await bot.wait_for('message', check=check, timeout=60)  # Wait for user response with a timeout
        await msg.delete()  # Delete the user's message to keep the chat clean
        action = int(msg.content)
        
        if action == 1:
            await slash_commands.add_record_prompt(interaction, bot)
        elif action == 2:
            await slash_commands.update_record_prompt(interaction, bot)
        elif action == 3:
            await slash_commands.remove_record_prompt(interaction, bot)
        elif action == 4:
            await slash_commands.view_watchlist(interaction, bot)
        elif action == 5:
            await interaction.followup.send("Action cancelled.", ephemeral=True)
        else:
            await interaction.followup.send("Invalid action. Please choose a number from the list.", ephemeral=True)
    except asyncio.TimeoutError:
        await interaction.followup.send("Action timed out. Please start again.", ephemeral=True)
    
    interaction_states[user_id] = 'completed'  # Reset state to completed
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