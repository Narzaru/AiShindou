import discord
from discord.ext import commands
import os


class CogWork(commands.Cog):

    def __init__(self, client, ext):
        # Extensions
        self.ext = ext
        # Bot class
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def unload_cogs_command(self, ctx):
        for item in self.ext:
            try:
                self.client.unload_extension(item)
            except Exception as e:
                await ctx.send(f"{type(e).__name__}, {e}")
        self.ext *= 0

    @commands.command()
    @commands.is_owner()
    async def load_cogs_command(self, ctx):
        self.ext.clear()
        for folder in os.listdir(path='./cogs'):
            for file in os.listdir(path=f'./cogs/{folder}'):
                if file.endswith('.py') and file[:-3] not in self.client.cogs.keys():
                    if file[:-3] != "reworkCogWork":
                        self.ext.append(f'cogs.{folder}.{file[:-3]}')
                        try:
                            self.client.load_extension(f'cogs.{folder}.{file[:-3]}')
                        except Exception as e:
                            await ctx.send(f"{type(e).__name__}, {e}")

    @commands.command()
    @commands.is_owner()
    async def reload_cogs_command(self, ctx):
        await self.unload_cogs_command(ctx)
        await self.load_cogs_command(ctx)


def setup(client):
    client.add_cog(CogWork(client, client.ext))
