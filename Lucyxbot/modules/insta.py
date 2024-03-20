from pyrogram import Client, filters
import requests
import os
from Lucyxbot import app

# Define a function to handle incoming messages
@app.on_message(filters.command("insta"))
async def download_instagram_post(client, message):
    # Extract the URL of the Instagram post from the message
    if len(message.command) < 2:
            await message.reply_text(
                "Example:/insta 'link of post you want to download'"
            )
    else:
        url = message.text.split(" ", 1)[1]

    # Pretend to download the Instagram post using requests module
    response = requests.get(url)

    if response.status_code == 200:
        # Save the downloaded content to a temporary file
        with open("temp_instagram_post.jpg", "wb") as f:
            f.write(response.content)
        
        # Send the saved file as a document to the user
        await message.reply_document("temp_instagram_post.jpg", caption="Here's your Instagram post!")

        # Delete the temporary file
        os.remove("temp_instagram_post.jpg")
    else:
        await message.reply("Failed to download the Instagram post. Please check the URL.")
