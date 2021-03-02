# https://discord.com/api/oauth2/authorize?client_id=761979460344872981&permissions=8&scope=bot
import os

import asyncio
import discord
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv
from settingsClass import JsonShell
from help import Help_command


class Initialization():
    def __init__(self):
        self.token = os.getenv('DISCORD_TOKEN')
        self.intents = None

    async def get_prefix(self, client, message):
        data = JsonShell('serversPrefixes.json')
        prefixes = data.get()
        try:
            return prefixes[str(message.guild.id)]
        except Exception:
            return 'Ai.', 'ai.'

    def set_none_intents(self):
        self.intents = Intents.none()
        return self

    def set_all_intents(self):
        self.intents = Intents.all()
        return self

    def set_default_intents(self):
        self.intents = Intents.default()
        return self

    def set_intent(self, key, value):
        if self.intents is None:
            print(f"[WARNING] intents not installed, it will be installed by default")
            self.set_default_intents()
        try:
            if value is True:
                self.intents.value = self.intents.value | self.intents.VALID_FLAGS.get(key)
            elif value is False:
                self.intents.value = self.intents.value & ~(self.intents.VALID_FLAGS.get(key))
            else:
                print(f"[WARNING] incorrecnt intent value({value})")
        except:
            print(f"[ERROR] intent by key({key}) not found or incorrecnt value({value})")
        return self

    def set_intents(self, **kwargs):
        for key, value in kwargs.items():
            self.set_intent(key, value)

    def get_intents(self):
        return self.intents

    def get_token(self):
        return self.token


class ClientBot(commands.Bot):
    def __init__(self, command_prefix, help_command, intents):
        commands.Bot.__init__(self, command_prefix=command_prefix, help_command=help_command, description=None, intents=intents)
    
    async def on_ready(self):
        print(f'\n{self.user} connected to the guild(s):')
        for guild in self.guilds:
            print(f'\t>{guild.name}(id: {guild.id})')

    def load_cogs(self):
        print('Loading cogs\n')
        for folder in os.listdir(path='./cogs'):
            print(folder)
            for file in os.listdir(path=f'./cogs/{folder}'):
                print(f'\t{file}')
                if file.endswith('.py'):
                    self.load_extension(f'cogs.{folder}.{file[:-3]}')


def main():
    initClass = Initialization()
    initClass.set_default_intents()
    initClass.set_intents(members=True, 
                          presences=True,
                          typing=False,
                          invites=False,
                          integrations=False,
                          guild_typing=False,
                          dm_typing=False,
                          dm_reactions=False,
                          dm_messages=False)
    client = ClientBot(command_prefix=initClass.get_prefix, help_command=Help_command(), intents=initClass.get_intents())
    client.load_cogs()
    client.run(initClass.get_token())


if __name__ == "__main__":
    main()


'''
webhooks:True
voice_states:True
typing:True
reactions:True
presences:False
messages:True
members:False
invites:True
integrations:True
guilds:True
guild_typing:True
guild_reactions:True
guild_messages:True
emojis:True
dm_typing:True
dm_reactions:True
dm_messages:True
'''
