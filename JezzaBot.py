import discord
from datetime import datetime

def handle_user_messages(msg) ->str:
    message = msg.lower() #Converts all inputs to lower case
    if(message == 'what is the time'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        time = (f"Current Time = {current_time}")
        return time

async def processMessage(message, user_message):
    try:
        botfeedback = handle_user_messages(user_message)
        await message.channel.send(botfeedback)
    except Exception as error:
        print(error)

def runBot():
    discord_token = 'MTI4NTg4MDY1OTMzMTY0OTU0Nw.GdiDI1.QsyFyudC8Gw_uyeuWymJWGTa77ghsy343z5SJs'
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print({client.user}, 'is live')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        await processMessage(message, 'what is the time')

    client.run(discord_token)