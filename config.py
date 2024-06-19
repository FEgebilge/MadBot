import json
import os

# Get the current directory of the script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the config.json file
config_path = os.path.join(base_dir, 'config', 'config.json')

# Load API keys from the config.json file
with open(config_path) as config_file:
    config = json.load(config_file)

# Access the API keys
DISCORD_TOKEN = config['DISCORD_TOKEN']
WEATHER_API_KEY = config['WEATHER_API_KEY']
YOUTUBE_API_KEY = config['YOUTUBE_API_KEY']
MOVIE_API_KEY = config['MOVIE_API_KEY']
GPT_API_KEY = config['GPT_API_KEY']