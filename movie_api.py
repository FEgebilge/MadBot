import requests
import config

def get_film_details(film_title):
    api_key = config.MOVIE_API_KEY
    url = f'http://www.omdbapi.com/?apikey={api_key}={film_title}'
    response = requests.get(url)
    data = response.json()
    print(data)
    return data
    

