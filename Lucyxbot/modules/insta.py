from pyrogram import Client, filters
import requests
from Lucyxbot import app

# Define a function to handle incoming messages
@app.on_message(filters.command("insta"))
async def download_instagram_post(client, message):
    # Extract the URL of the Instagram post from the message
    url = message.text.split(" ", 1)[1]

    # Pretend to download the Instagram post using requests module
    response = requests.get(url)

    if response.status_code == 200:
        # Send the downloaded content as a file to the user
        await message.reply_document(response.content, caption="Here's your Instagram post!")
    else:
        await message.reply("Failed to download the Instagram post. Please check the URL.")
