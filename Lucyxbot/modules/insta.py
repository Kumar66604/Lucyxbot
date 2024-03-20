from pyrogram import Client, filters
import requests
import os

# Define the RapidAPI endpoint URL
RAPIDAPI_URL = "https://instagram310.p.rapidapi.com/post"

# Function to download media from Instagram using RapidAPI
async def download_instagram_media(message, url):
    headers = {
        "X-RapidAPI-Key": "dc941af14dmsh6bc574712f93787p1be962jsn87965c569abb",  # Replace with your RapidAPI key
        "X-RapidAPI-Host": "instagram310.p.rapidapi.com"
    }
    params = {"url": url}
    
    try:
        response = requests.get(RAPIDAPI_URL, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Assuming the response contains the media file
        media_content = response.content
        
        # Save the media content to a file
        file_name = f"instagram_media.{response.headers['Content-Type'].split('/')[-1]}"
        with open(file_name, "wb") as file:
            file.write(media_content)
        
        # Send the media file to the user
        await message.reply_document(file_name)
        
        # Clean up: Delete the downloaded file
        os.remove(file_name)
        
    except requests.exceptions.RequestException as e:
        await message.reply(f"Error downloading media: {e}")

# Define a command handler to trigger the media download
@app.on_message(filters.command("insta"))
async def trigger_download(client, message):
    try:
        # Extract the Instagram post URL from the command
        url = message.text.split(" ", 1)[1]
        
        # Call the function to download and send the media
        await download_instagram_media(message, url)
        
    except IndexError:
        await message.reply("Please provide the URL of the Instagram post.")

