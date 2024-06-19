import discord
import random
import weather_api
import movie_api
import gpt_api
import lists
import asyncio
import time
import http.client
from PIL import Image, ImageDraw, ImageFont



async def hello(interaction:discord.Interaction):
    message= f"{random.choice(lists.hello_list)} {interaction.user.mention}"        
    await interaction.response.send_message(message)


async def help(interaction:discord.Interaction):
    dm_channel = await interaction.user.create_dm()
    await dm_channel.send("This is a temporary help message")
    await interaction.response.send_message("Help message sent to your DM", ephemeral=True)


async def reaction(interaction: discord.Interaction):
    await interaction.response.send_message("Reaction message response")
    channel = interaction.channel
    message = await channel.send("Message Sent")
    emoji = "\N{THUMBS UP SIGN}"  # Number 1 emoji code
    await message.add_reaction(emoji)


async def weather(interaction:discord.Interaction,location:str):
    weather_data = weather_api.get_weather(location)
    print(weather_data)
    embed=discord.Embed(
        title=f"Weather: {weather_data['location']['name']}",
        description=f"Temperature: {weather_data['current']['temp_c']} ℃ \n Condition: {weather_data['current']['condition']['text']}",
        color=discord.Colour.dark_blue()
        )
    thumbnail_url = f"https:{weather_data['current']['condition']['icon']}"
    print(thumbnail_url)
    embed.set_thumbnail(url=thumbnail_url)
    embed.set_footer(text=f"Feels like: {weather_data['current']['feelslike_c']} ℃\nWind: {weather_data['current']['wind_kph']} km/h \nHumidity: {weather_data['current']['humidity']}%")
    await interaction.response.send_message(embed=embed)


async def movie(interaction:discord.Interaction,movie_to_search:str):
        film_data = movie_api.get_film_details(movie_to_search)
        if film_data['Response'] == 'True':
            embed=discord.Embed(
                title=f"{film_data['Title']}-{film_data['Year']}",
                description=f"Duration: {film_data['Runtime']}\n Genres:{film_data['Genre']}\n Metascore:{film_data['Metascore']}\n IMDB: {film_data['imdbRating']}",
                color=discord.Colour.random()
            )
            embed.set_author(name=interaction.user)
            embed.set_footer(text=film_data['Plot'] if 'Plot' in film_data else 'No plot available')
            embed.set_image(url=film_data['Poster']if 'Poster' in film_data else '')
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Film not found :( ")



async def poll(interaction: discord.Interaction,heading:str ,options: str):
    option_list = options.split(",")  # Split the options by ,
    if len(option_list) < 2:
        await interaction.response.send_message("Please provide at least two options for the poll.")
        return
    
    await interaction.response.send_message("Poll started!")
    channel = interaction.channel
    poll_message = ""
    for i, option in enumerate(option_list, start=1):
        poll_message += f"{i}. {option.strip()}\n"
    
    embed=discord.Embed(
        title=heading,
        description=poll_message,
        color=discord.Colour.dark_red()
    )
    message_to_react = await channel.send(embed=embed)

    for i in range(1, len(option_list) + 1):
        emoji = f"{i}\u20e3"  # Using number emojis
        await message_to_react.add_reaction(emoji)
    

async def who_is_right(interaction: discord.Interaction, timeout: int):
    channel = interaction.channel
    embed = discord.Embed(
        title="Who is right?",
        description=f"timeout: {timeout} seconds.!",
        color=discord.Colour.dark_teal()
        )
    attendance_emoji = "\U0000270B"
    message = await channel.send(embed=embed)
    await message.add_reaction(attendance_emoji)
    await asyncio.sleep(timeout)
    message = await channel.fetch_message(message.id)  # Refresh the message object
    attendance_reaction = discord.utils.get(message.reactions, emoji=attendance_emoji)
    if attendance_reaction:
        users = []
        async for user in attendance_reaction.users():
            users.append(user)
        
        print("Users who reacted with {}:".format(attendance_emoji))
        for user in users:
            print(user.name)

        if len(users) > 1:
            users.pop(0)
            winner = random.choice(users)
            print("Randomly selected winner: {}".format(winner.name))
            await channel.send("{} is right".format(winner.mention))
        else:
            await channel.send("No one clicked the attendance emoji.")


   
async def gpt_command(interaction: discord.Interaction, chat:str):
    # Make a request to the GPT API
    response = gpt_api.generate_text(chat)
    await interaction.response.send_message(response)


async def send_image(interaction:discord.Interaction):
    with open("demo_image.jpg",'rb') as f:
        image_file= discord.File(f,filename="demo_image.jpg")
    await interaction.response.send_message(file=image_file)


async def ping(host, interaction:discord.Interaction):
    try:
        start_time = time.time()
        conn = http.client.HTTPConnection(host)
        conn.request("GET", "/")
        response = conn.getresponse()
        end_time = time.time()
        latency = end_time - start_time
        embed=discord.Embed(
                title="Ping",
                description=f"Latency:{latency*1000 :.2f}ms \n Site:{host}",
                color=discord.Colour.random()
            )
        await interaction.response.send_message(embed=embed)
        return latency * 1000  # Convert to milliseconds
    except Exception as e:
        return None
    
async def meme_generator(interaction: discord.Interaction, text: str,y_position:int,name:str):
    image = Image.open(f"meme_{name}.jpg")
    draw = ImageDraw.Draw(image)
    text_color = (255, 255, 255)
    text_to_draw = text
    font_size = 100
    font = ImageFont.truetype("impact.ttf", size=font_size)
    position = (0, 0)

    # Calculate the bounding box of the text
    text_box = draw.textbbox((0, 0), text_to_draw, font=font)

    # Calculate the text width and height
    text_width = text_box[2] - text_box[0]
    text_height = text_box[3] - text_box[1]

    # Center x-axis
    image_width, _ = image.size
   
    # Reduce font size 
    while text_width > image_width:
        font_size -= 2
        font = ImageFont.truetype("impact.ttf", size=font_size)

        text_box = draw.textbbox((0, 0), text_to_draw, font=font)
        text_width = text_box[2] - text_box[0]
        text_height = text_box[3] - text_box[1]


    x = (image_width - text_width) // 2

    # Calculate y position
    y = (image.height - text_height) // 2

    # Update the position
    position = (x, y_position)

    draw.text(position, text_to_draw, font=font, fill=text_color)

    image.save("generated_image.jpg")

    with open("generated_image.jpg", "rb") as f:
        image_file = discord.File(f, filename="generated_image.jpg")

    await interaction.response.send_message(file=image_file)

