import io
import aiohttp
import discord
from discord.ext import commands
from discord import utils


class OnBehalfBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def send(self, ctx, messageID, fromChannelID=None, toChannelID=None):
        if fromChannelID is None or fromChannelID == 'this':
            fromChannel = ctx.channel
        else:
            fromChannel = utils.get(ctx.guild.text_channels, id=int(fromChannelID))
        if toChannelID is None or toChannelID == 'this':
            toChannel = ctx.channel
        else:
            toChannel = utils.get(ctx.guild.text_channels, id=int(toChannelID))
        commadMessage = ctx.message
        copiedMessage = await fromChannel.fetch_message(messageID)
        if len(copiedMessage.attachments) > 0:
            imageURL = copiedMessage.attachments[0].url
            async with aiohttp.ClientSession() as session:
                async with session.get(imageURL) as resp:
                    if resp.status != 200:
                        return await ctx.send('Не получилось скачать изображение')
                    image = io.BytesIO(await resp.read())
            await toChannel.send(f'{copiedMessage.content}', file=discord.File(image, 'cool_image.png'))
        else:
            await toChannel.send(f'{copiedMessage.content}')
            await commadMessage.delete()
            await copiedMessage.delete()

    @commands.command()
    async def react(self, ctx, reaction, messageID=None, channelID=None):
        if channelID is not None or channelID == 'this':
            channel = ctx.channel
        else:
            channel = utils.get(ctx.guild.text_channels, id=int(channelID))
        commandMessage = ctx.message
        message = await channel.fetch_message(messageID)
        await message.add_reaction(str(reaction))
        await commandMessage.delete()


def setup(client):
    client.add_cog(OnBehalfBot(client))
