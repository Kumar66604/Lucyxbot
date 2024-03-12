


@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("Hello! I am your bot. How can I help you?")
