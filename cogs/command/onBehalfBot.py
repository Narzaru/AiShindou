import io
import aiohttp
import asyncio
import os
import discord
from discord.ext import commands
from discord import utils
from settingsClass import JsonShell

class OnBehalfBot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def send(self, ctx , messageID, channelID = None):

        if channelID == None or channelID == 'this':
            channel = ctx.channel
        else:
            channel = utils.get(ctx.guild.text_channels, id=int(channelID))
        commadMessage = ctx.message
        copiedMessage = await channel.fetch_message(messageID)

        if len(copiedMessage.attachments) > 0:
            imageURL = copiedMessage.attachments[0].url
            async with aiohttp.ClientSession() as session:
                async with session.get(imageURL) as resp:
                    if resp.status != 200:
                        return await ctx.send('Не получилось скачать изображение')
                    image = io.BytesIO(await resp.read())
            await ctx.send(f'{copiedMessage.content}', file=discord.File(image, 'cool_image.png'))
        else:
            await ctx.send(f'{copiedMessage.content}')

            await commadMessage.delete()
            await copiedMessage.delete()

    @commands.command()
    async def react(self, ctx, reaction, messageID = None, channelID = None):

        if channelID == None or channelID == 'this':
            channel = ctx.channel
        else:
            channel = utils.get(ctx.guild.text_channels, id=int(channelID))

        commandMessage = ctx.message
        message = await channel.fetch_message(messageID)

        await message.add_reaction(str(reaction))
        await commandMessage.delete()

def setup(client):
    client.add_cog(OnBehalfBot(client))