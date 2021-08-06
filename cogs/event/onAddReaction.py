from discord import utils
from discord.ext import commands
from service.utils import JsonShell
from service.sql import sqlite, Factory


class ReactionHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if self.client.user.id != payload.user_id:
            db = sqlite("D:\\python\\Ai Shindou\\service\\discordBot.db")
            data = db.select(columns_name="prefix", table_name="prefixes", factory=Factory.string_factory)
            print(data[0])
            file = JsonShell('service\\serversSettings.json')
            data = file.get_data()
            serverData = data[str(payload.guild_id)]
            if payload.message_id == int(serverData['RULE_MESSAGE_ID']):
                await self.set_guest(payload)
            if payload.message_id == int(serverData['ROLE_MESSAGE_ID']):
                await self.set_roles(payload)

    async def set_guest(self, payload):
        file = JsonShell('service\\serversSettings.json')
        data = file.get_data()
        serverData = data[str(payload.guild_id)]
        try:
            guild = self.client.get_guild(payload.guild_id)
            channel = guild.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            member = payload.member
            role = utils.find(lambda role: role.id == int(serverData['RULE_ACCEPT_ROLE']), guild.roles)
            ruleEmoji = serverData['RULE_ACCEPT_EMOJI']
            if (ruleEmoji == payload.emoji.name):
                if (len([i for i in member.roles if i == role]) == 1):
                    await member.remove_roles(role)
                    print(f'[{guild.name}]{member.name} was removed {role.name}')
                else:
                    await member.add_roles(role)
                    print(f'[{guild.name}]{member.name} was granted {role.name}')
            await message.remove_reaction(payload.emoji, member)
        except KeyError:
            await message.remove_reaction(payload.emoji, member)

    async def set_roles(self, payload):
        file = JsonShell('service\\serversSettings.json')
        data = file.get_data()
        serverData = data[str(payload.guild_id)]
        try:
            guild = self.client.get_guild(payload.guild_id)
            channel = guild.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            member = payload.member
            roleEmoji = serverData['ROLE_BY_EMOJI']
            role = utils.find(lambda role: role.id == int(roleEmoji[payload.emoji.name]), guild.roles)
            if(len([i for i in member.roles if i.id not in serverData["EXCLUDE_ROLES"]]) <= int(serverData["MAX_ROLE_PER_USER"])):
                if (len([i for i in member.roles if i == role]) == 1):
                    await member.remove_roles(role)
                    print(f'[{guild.name}]{member.name} was removed {role.name}')
                else:
                    await member.add_roles(role)
                    print(f'[{guild.name}]{member.name} was granted {role.name}')
                await message.remove_reaction(payload.emoji, member)
            else:
                await message.remove_reaction(payload.emoji, member)
        except KeyError:
            await message.remove_reaction(payload.emoji, member)


def setup(client):
    client.add_cog(ReactionHandler(client))
