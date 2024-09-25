import os
import discord
from typing import Final
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

def handle_user_messages(msg) ->str:
    message = msg.lower() #Converts all inputs to lower case
    if(message == 'what is the time'):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        time = (f"Current Time: {current_time}")
        return time

async def processMessage(message, user_message):
    try:
        botfeedback = handle_user_messages(user_message)
        await message.channel.send(botfeedback)
    except Exception as error:
        print(error)

def runBot():
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print({client.user}, 'is running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        await processMessage(message, 'what is the time')

    client.run(TOKEN)
