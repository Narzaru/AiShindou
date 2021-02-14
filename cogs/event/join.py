import asyncio
import datetime
import json
import random

import discord
import pytz
from discord.ext import commands
from settingsClass import JsonShell


class JoinEvents(commands.Cog):


    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        if (member != None):
            print(f'{member} has joined a server:')
            print(f'{member.guild}(id: {member.guild.id})')
            await self.__welcome(member=member)


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if (member != None):
            print(f'{member} has left a server:')
            print(f'{member.guild}(id: {member.guild.id})')
            await self.__goodbye(member=member)


    @commands.command()
    async def test(self, ctx):
        await self.__welcome(ctx.author)


    async def __welcome(self, member : discord.member):
        file = JsonShell('serversSettings.json')
        data = file.get()
        serverData = data[str(member.guild.id)]
        welcomeReactions = serverData['WELCOME_CHANNEL_REACTION']

        # Welcome embed
        embed=discord.Embed(
            title='Встречайте новенького!',
            description=f'Ня, {member.mention}!\n{member.name}{random.choice(welcomeReactions)}',
            color=0x32a852 # https://www.colorhexa.com/32a852 hex color
            )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_image(url='https://i.gifer.com/L5I9.gif')
        embed.set_footer(
            text='Времечко',
            icon_url='https://i.imgur.com/cb7rB5Y.png'
            )
        embed.timestamp = datetime.datetime.now(pytz.timezone('Etc/Greenwich'))


        # Message send
        channel = member.guild.get_channel(int(serverData['WELCOME_CHANNEL_ID']))
        await channel.send(embed=embed)


    async def __goodbye(self,member : discord.member):
        file = JsonShell('serversSettings.json')
        data = file.get()
        serverData = data[str(member.guild.id)]

        embed=discord.Embed(
            title='Прощай, буду скучать по тебе!',
            description=f'Прощай, надеюсь ещё увидимся {member.name}',
            color=0xDC143C # https://www.colorhexa.com/dc143c hex color
            )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(
            text='Времечко',
            icon_url='https://i.imgur.com/cb7rB5Y.png'
            )
        embed.set_image(url='https://i.gifer.com/L5IB.gif')
        embed.timestamp = datetime.datetime.now(pytz.timezone('Etc/Greenwich'))
        channel = member.guild.get_channel(int(serverData['WELCOME_CHANNEL_ID']))
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(JoinEvents(client))
