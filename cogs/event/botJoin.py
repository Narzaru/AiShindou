from settingsClass import JsonShell
from discord.ext import commands


class BotJoin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            await self.add_default_prefix(guild)
            await self.add_default_settings(guild)
        except KeyError:
            print('[ERROR] on_guild_join key error')

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            await self.remove_default_prefix(guild)
            await self.remove_default_settings(guild)
        except KeyError:
            print('[ERROR] on_guild_remove key error')

    async def add_default_prefix(self, guild):
        data = JsonShell('serversSettings.json')
        data.put(data)

    async def add_default_settings(self, guild):
        data = JsonShell('serversSettings.json')
        settings = data.get_data()
        settings[str(guild.id)] = {
            'WELCOME_CHANNEL_ID': None,
            'WELCOME_CHANNEL_REACTION': [None],

            'RULE_MESSAGE_ID': None,
            'RULE_ACCEPT_EMOJI': None,
            'RULE_ACCEPT_ROLE': None,

            'ROLE_MESSAGE_ID': None,
            'ROLE_BY_EMOJI': None,

            'EXCLUDE_ROLES': None,
            'MAX_ROLE_PER_USER': None,

            'ROLE_ADMIN': {
                'NAME': None,
                'ID': None
            }
        }

    async def remove_default_prefix(self, guild):
        pass

    async def remove_default_settings(self, guild):
        pass


def setup(client):
    client.add_cog(BotJoin(client))
