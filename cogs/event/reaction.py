import asyncio
import random
import discord
from discord import utils
from discord.ext import commands
import config

class Reaction(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == config.RULE_MESSAGE_ID:
            await self.__guest_role_add(payload=payload)
        elif payload.message_id == config.ROLE_MESSAGE_ID:
            await self.__reaction_role_add(payload)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == config.RULE_MESSAGE_ID:
            await self.__guest_role_remove(payload=payload)
        elif payload.message_id == config.ROLE_MESSAGE_ID:
            await self.__reaction_role_remove(payload)

#Обработка сообщений с правилами
    async def __guest_role_add(self, payload):
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        emoji = str(payload.emoji)
        member = utils.get(message.guild.members, id=payload.user_id)

        if emoji == config.RULE_ACCEPT_EMOJI:
            role = utils.get(message.guild.roles, id=config.RULE_ACCEPT_ROLE)
            if role == None:
                print('[ERROR] RULE ROLE NOT FOUND')
                return
            else:
                #if len([roles for roles in member.roles if roles.id not in config.ROLE_EXCEPTION]) <= config.ROLE_MAX_NUMBER_ROLE_PER_USER:
                await member.add_roles(role)
                print(f'[SUCCES] {member.name} was granted role: {role.name} ')
        else:
            await message.remove_reaction(emoji, member)

    async def __guest_role_remove(self, payload):
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        emoji = str(payload.emoji)
        member = utils.get(message.guild.members, id=payload.user_id)

        if emoji == config.RULE_ACCEPT_EMOJI:
            role = utils.get(message.guild.roles, id=config.RULE_ACCEPT_ROLE)
            if role == None:
                print('[ERROR] RULE ROLE NOT FOUND')
                return
            await member.remove_roles(role)
            print(f'[SUCCES] {member.name} taked away role: {role}')
            return
        else:
            await message.remove_reaction(emoji, member)

#Обработка сообщения с реакциями по ролям
    async def __reaction_role_add(self, payload):
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        emoji = str(payload.emoji)
        member = utils.get(message.guild.members, id=payload.user_id)

        try:
            if len([roles for roles in member.roles if roles.id not in config.ROLE_EXCEPTION]) <= config.ROLE_MAX_NUMBER_ROLE_PER_USER:
                role = utils.get(member.guild.roles, id=config.ROLE_EMOJI_ROLE[emoji])
        except KeyError:
            print(f'[WARNING] Role by Emoji {emoji} not found')
            await message.remove_reaction(emoji, member)
            return
        await member.add_roles(role)

    async def __reaction_role_remove(self, payload):
        channel = self.client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        emoji = str(payload.emoji)
        member = utils.get(message.guild.members, id=payload.user_id)
        try:
            role = utils.get(member.guild.roles, id=config.ROLE_EMOJI_ROLE[emoji])
        except KeyError:
            return
        await member.remove_roles(role)

def setup(client):
    client.add_cog(Reaction(client))