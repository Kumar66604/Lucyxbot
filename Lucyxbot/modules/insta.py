from pyrogram import Client, filters
import requests
import os
import mimetypes
from urllib.parse import urlparse
from Lucyxbot import app

# Define a function to handle incoming messages
@app.on_message(filters.command("insta"))
async def download_instagram_post(client, message):
    # Extract the URL of the Instagram post from the message
    try:
        url = message.text.split(" ", 1)[1]
    except IndexError:
        await message.reply("Please provide the URL of the Instagram post.")
        return

    # Pretend to download the Instagram post using requests module
    response = requests.get(url)

    if response.status_code == 200:
        # Extracting the file extension from the URL
        parsed_url = urlparse(url)
        file_extension = os.path.splitext(parsed_url.path)[1]

        # Check if the Instagram post is a video
        if "video" in response.headers.get("content-type", ""):
            # It's a video, send it as a video
            await message.reply_video(url)
        else:
            # It's an image, send it as a photo
            await message.reply_photo(url)
    else:
        await message.reply("Failed to download the Instagram post. Please check the URL.")
            
