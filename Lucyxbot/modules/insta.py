from pyrogram import Client, filters
from io import BytesIO
import requests
from Lucyxbot import app

# Define the RapidAPI endpoint URL
RAPIDAPI_URL = "https://instagram310.p.rapidapi.com/post"

# Function to download and send video from Instagram using RapidAPI
async def download_instagram_video(message, url):
    headers = {
        "X-RapidAPI-Key": "dc941af14dmsh6bc574712f93787p1be962jsn87965c569abb",  # Replace with your RapidAPI key
        "X-RapidAPI-Host": "instagram310.p.rapidapi.com"
    }
    params = {"url": url}
    
    try:
        response = requests.get(RAPIDAPI_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Get the video URL from the response JSON
        video_url = response.json()['data'][0]['download']
        
        # Download the video content
        video_content = BytesIO(requests.get(video_url).content)
        
        # Set the file name to your app username
        video_content.name = f"{app.me.username}.mp4"
        
        # Send the video to the user
        await message.reply_video(video=video_content)
        
    except requests.exceptions.RequestException as e:
        await message.reply(f"Error downloading video: {e}")

# Define a command handler to trigger the video download
@app.on_message(filters.command("/ig"))
async def trigger_video_download(client, message):
    try:
        # Extract the Instagram post URL from the command
        url = message.text.split(" ", 1)[1]
        
        # Call the function to download and send the video
        await download_instagram_video(message, url)
        
    except IndexError:
        await message.reply("Please provide the URL of the Instagram post.")

# Run the Pyrogram client
app.run()
