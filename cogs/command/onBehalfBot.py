import io
import aiohttp
import asyncio
import os
import discord
from discord.ext import commands
from discord import utils
import config

class OnBehalfBot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        await ctx.send(embed = discord.Embed(description =
        f'**Ой-ой, прости, <@{ctx.author.id}>, но такой команды не существует.**', color = discord.Color.red())
        )

    @commands.command()
    @commands.has_role(config.ROLE_ADMIN)
    async def send(self, ctx, messageID, channelName = None, deleteMessage = False):

        if channelName == None or channelName == 'this':
            channel = ctx.channel
        else:
            channel = utils.get(ctx.guild.text_channels, name=channelName)
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

        if not deleteMessage:
            await commadMessage.delete()
        else:
            await commadMessage.delete()
            await copiedMessage.delete()

    @commands.command()
    @commands.has_role(config.ROLE_ADMIN)
    async def react(self, ctx, messageID, reaction ,channelName = None):

        if channelName == None or channelName == 'this':
            channel = ctx.channel
        else:
            channel = utils.get(ctx.guild.text_channels, name=channelName)

        commandMessage = ctx.message
        message = await channel.fetch_message(messageID)

        await message.add_reaction(str(reaction))
        await commandMessage.delete()

def setup(client):
    client.add_cog(OnBehalfBot(client))