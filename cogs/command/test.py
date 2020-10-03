import asyncio
import os
import discord
from discord.ext import commands
import config

class Test(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(embed = discord.Embed(description =
        f'**Булин ? <@{ctx.author.id}>, такой команды не существует.**', color = discord.Color.red())
        )

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f'fine test <@{ctx.author.id}>')

    @commands.command()
    async def test_owner(self, ctx):
        pass

def setup(client):
    client.add_cog(Test(client))