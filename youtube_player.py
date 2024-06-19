"""
import discord
import asyncio
import youtube_dl
import os

async def play_youtube(interaction: discord.Interaction, query: str):
    # Get the user's voice channel from the interaction object
    channel = interaction.user.voice.channel

    # Check if the user is in a voice channel
    if channel is None:
        await interaction.response.send_message("You are not connected to a voice channel.")
        return

    # Connect to the voice channel
    voice_client = await channel.connect()

    try:
        # Create a temporary filename for the audio
        audio_filename = "audio.mp3"

        # Create a YouTube DL extractor instance
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                'outtmpl': audio_filename,
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # Extract information about the video
            info = ydl.extract_info(query, download=True)

        # Get the path to the downloaded audio file
        audio_path = os.path.abspath(audio_filename)

        # Start streaming the audio
        voice_client.stop()  # Stop any currently playing audio
        voice_client.play(discord.FFmpegPCMAudio(audio_path))

        # Wait for the audio to finish playing
        while voice_client.is_playing() or voice_client.is_paused():
            await asyncio.sleep(1)

    finally:
        # Cleanup resources
        voice_client.stop()
        await voice_client.disconnect()

        # Delete the downloaded audio file
        os.remove(audio_path)
"""