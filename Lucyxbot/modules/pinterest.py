from pyrogram import Client, filters
from io import BytesIO
import requests
from Lucyxbot import app
from config import RAPID_APIKEY

# Define the RapidAPI endpoint URL
RAPIDAPI_URL = "https://pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com/api/data"

# Function to download and send video from Pinterest using RapidAPI
async def download_pinterest_video(message, url):
    headers = {
        "X-RapidAPI-Key": RAPID_APIKEY,
        "X-RapidAPI-Host": "pinterest-downloader-download-pinterest-image-video-and-reels.p.rapidapi.com"
    }
    params = {"url": url}
    
    try:
        api_response = requests.get(RAPIDAPI_URL, headers=headers, params=params)
        api_response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Check if the response is in JSON format
        if api_response.headers.get('content-type') == 'application/json':
            # Get the video URL from the response JSON
            video_url = api_response.json().get('data', [])[0].get('download')
            
            if video_url:
                # Download the video content
                video_content = BytesIO(requests.get(video_url).content)
                video_content.name = f"{app.me.username}.mp4"
                
                # Send the video to the user
                await message.reply_video(video=video_content)
            else:
                await message.reply("No video found in the response.")
        else:
            await message.reply("Invalid response format from the RapidAPI endpoint.")
        
    except requests.exceptions.RequestException as e:
        await message.reply(f"Error downloading video: {e}")

# Define a command handler to trigger the video download
@app.on_message(filters.command("pn"))
async def trigger_video_download(client, message):
    try:
        # Extract the Pinterest post URL from the command
        url = message.text.split(" ", 1)[1]
        
        # Call the function to download and send the video
        await download_pinterest_video(message, url)
        
    except IndexError:
        await message.reply("Please provide the URL of the Pinterest post.")
                  
