import requests
import config

api_key = config.WEATHER_API_KEY
endpoint = 'https://api.weatherapi.com/v1/current.json'


    
def get_weather(input_location):
    
    params = {
    'key': api_key,
    'q': input_location
    }
    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        data = response.json()
        # Access the data and perform further actions
        return data




""""        
        location = data['location']['name']
        temperature = data['current']['temp_c']
        condition = data['current']['condition']['text']
    weather_item={
        'location':location,
        'temperature':temperature,
        'condition':condition
    }

    return weather_item


"""