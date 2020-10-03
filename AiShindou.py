import os
import discord
from discord.ext import commands
import config
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot('bulin.')

@client.event
async def on_ready():
    for guild in client.guilds:
        print(f'{client.user} connected to the guild:')
        print(f'{guild.name}(id: {guild.id})')

@client.command()
@commands.has_role(config.ROLE_ADMIN)
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
@commands.has_role(config.ROLE_ADMIN)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.has_role(config.ROLE_ADMIN)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

def load_cogs():
    print('Cog`s folder structure:')
    for folder in os.listdir(path='./cogs'):
        print(f'┠{folder}')
        for file in os.listdir(path=f'./cogs/{folder}'):
            if file.endswith('.py'):
                print(f'┠──{file[:-3]}')
                client.load_extension(f'cogs.{folder}.{file[:-3]}')

#RUN
load_cogs()
client.run(os.getenv('DISCORD_TOKEN'))