import bot
import config

def main():
    print("Weather API Key:", config.WEATHER_API_KEY)
    print("YouTube API Key:", config.YOUTUBE_API_KEY)
    print("Movie API Key:", config.MOVIE_API_KEY)
    print("GPT API Key:", config.GPT_API_KEY)

if __name__ == '__main__':
    bot.run_discord_bot()

