import asyncio
import random
import discord
from discord import utils
from discord.ext import commands
import config

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

    async def __welcome(self, member : discord.member):
        embed=discord.Embed(
            title='Встречайте новенького!',
            description=f'Ня, {member.mention}!\n{member.name} {random.choice(config.WELCOME_REACTION)}',
            color=0x32a852
            )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(
            text='gif by Seseren',
            icon_url='https://pbs.twimg.com/profile_images/835117601676144641/mYxxpLOk_400x400.jpg'
            )
        embed.set_image(url='https://i.gifer.com/L5I9.gif')

        channel = member.guild.get_channel(config.WELCOME_CHANNEL_ID)
        await channel.send(embed=embed)

    async def __goodbye(self,member : discord.member):
        embed=discord.Embed(
            title='Прощай, буду скучать по тебе!',
            description=f'Прощай, надеюсь ещё увидимся {member.name}',
            color=0xffbfba
            )
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(
            text='gif by Seseren',
            icon_url='https://pbs.twimg.com/profile_images/835117601676144641/mYxxpLOk_400x400.jpg'
            )
        embed.set_image(url='https://i.gifer.com/L5IB.gif')

        channel = member.guild.get_channel(config.WELCOME_CHANNEL_ID)
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(JoinEvents(client))