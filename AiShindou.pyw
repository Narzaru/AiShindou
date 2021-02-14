# https://discord.com/api/oauth2/authorize?client_id=761979460344872981&permissions=8&scope=bot
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from settingsClass import JsonShell


# Finding a guild prefix in the list (serversPrefixes)
def get_prefix(client, message):
    data = JsonShell('serversPrefixes.json')
    prefixes = data.get()
    try:
        return prefixes[str(message.guild.id)]
    except Exception:
        return 'Ai.', 'ai.'


# Initialize bot
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=get_prefix, intents=intents)


# On bot`s Ready event
@client.event
async def on_ready():
    print(f'{client.user} connected to the guild(s):')
    for guild in client.guilds:
        print(f'\t>{guild.name}(id: {guild.id})')


# Loading cogs
def load_cogs():
    for folder in os.listdir(path='./cogs'):
        for file in os.listdir(path=f'./cogs/{folder}'):
            if file.endswith('.py'):
                client.load_extension(f'cogs.{folder}.{file[:-3]}')


# RUN
def botInit():
    print('Loading cogs')
    load_cogs()
    print('Loading env')
    load_dotenv()
    client.run(os.getenv('DISCORD_TOKEN'))


botInit()
