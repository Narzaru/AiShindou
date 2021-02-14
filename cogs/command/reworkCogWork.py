# import discord
# import asyncio
# import os
from discord.ext import commands
# import subprocess


class CogWork(commands.Cog):

    def __init__(self, client):
        self.client = client

    '''@commands.command()
    @commands.has_role(item=config.ROLE_TECH_ADNIN['id'])
    async def listdir(self, ctx, directory = ''):
        dir = '.' + directory
        output = ''
        try:
            for folder in os.listdir(path=dir):
                if folder[0] != '_' and folder[0] != '.':
                    output += '|-' + folder + '\n'
            await ctx.send(f'Моя структура папок, ~сенпай!\n```{output}```')
        except FileNotFoundError:
            await ctx.send(f'Папка не найдена!')

    @commands.command()
    @commands.has_role(item=config.ROLE_TECH_ADNIN['id'])
    async def herokuLogs(self,ctx):
        await ctx.send(subprocess.check_output("heroku logs", shell=True))

    @commands.command()
    @commands.has_role(item=config.ROLE_TECH_ADNIN['id'])
    async def load(self, ctx, extension):
        self.client.load_extension(f'{extension}')

    @commands.command()
    @commands.has_role(item=config.ROLE_TECH_ADNIN['id'])
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'{extension}')

    @commands.command()
    @commands.has_role(item=config.ROLE_TECH_ADNIN['id'])
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'{extension}')
        self.client.load_extension(f'{extension}')'''


def setup(client):
    client.add_cog(CogWork(client))
