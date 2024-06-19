# MadBot Discord Bot 

## Description
This project is a Python-based discord application that integrates several APIs to offer functionalities such as weather updates and movie information retrieval. The project is modular, making it easy to extend and maintain.

## Features
- **Slash Commands**: Handles custom slash commands.
- **Weather API**: Fetches current weather information.
- **Movie API**: Retrieves movie information.
- **YouTube Player**: Controls YouTube playback.
- **GPT API**: Interacts with the GPT model for various tasks.
- **Lists Management**: Manages and manipulates lists.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/FEgebilge/MadBot.git
    ```
2. Navigate to the project directory:
    ```bash
    cd MadBot
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Setting Up Configuration File**
   - Create a `config` directory in the project root.
   - Create a `config.json` file inside the `config` directory and add your API keys:
     ```json
     {
         "WEATHER_API_KEY": "your_weather_api_key",
         "YOUTUBE_API_KEY": "your_youtube_api_key",
         "MOVIE_API_KEY": "your_movie_api_key",
         "GPT_API_KEY": "your_gpt_api_key"
     }
     ```

2. **Running the Application**
   - Run the main script:
     ```bash
     python main.py
     ```

## Project Structure
- `bot.py`: Contains the main bot functionality.
- `config.py`: Loads and provides access to API keys.
- `config/config.json`: Stores API keys.
- `gpt_api.py`: Handles interactions with the GPT API.
- `impact.ttf`: Font file used in the project.
- `lists.py`: Manages lists.
- `main.py`: The main entry point of the application.
- `movie_api.py`: Interacts with the movie API.
- `slash_commands.py`: Handles slash commands.
- `weather_api.py`: Interacts with the weather API.
- `youtube_player.py`: Controls YouTube playback.
- `response.json`: Sample response data.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.