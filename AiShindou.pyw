# https://discord.com/api/oauth2/authorize?client_id=761979460344872981&permissions=8&scope=bot
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from settingsClass import JsonShell
from help import Help_command


class Initialization():
    def __init__(self):
        load_dotenv()
        self.__token = os.getenv("DISCORD_TOKEN")
        self.__intents = None

    async def get_prefix(self, client, message):
        data = JsonShell('serversPrefixes.json')
        prefixes = data.get()
        try:
            return prefixes[str(message.guild.id)]
        except Exception:
            return 'Ai.', 'ai.'

    def set_none_intents(self):
        self.__intents = discord.Intents.none()
        return self

    def set_all_intents(self):
        self.__intents = discord.Intents.all()
        return self

    def set_default_intents(self):
        self.__intents = discord.Intents.default()
        return self

    def set_intent(self, key, value):
        if self.__intents is None:
            print(f"[WARNING] intents not installed, it will be installed by default")
            self.set_default_intents()
        try:
            if value is True:
                self.__intents.value = self.__intents.value | self.__intents.VALID_FLAGS.get(key)
            elif value is False:
                self.__intents.value = self.__intents.value & ~(self.__intents.VALID_FLAGS.get(key))
            else:
                print(f"[WARNING] incorrecnt intent value({value})")
        except Exception as e:
            print(f"{type(e).__name__}, {e}")
        return self

    def set_intents(self, **kwargs):
        for key, value in kwargs.items():
            self.set_intent(key, value)

    def get_intents(self):
        return self.__intents

    def get_token(self):
        return self.__token


class ClientBot(commands.Bot):
    def __init__(self, command_prefix, help_command, intents):
        self.ext = []
        commands.Bot.__init__(self, command_prefix=command_prefix, help_command=help_command, description=None, intents=intents)

    async def on_ready(self):
        print(f'\n{self.user} connected to the guild(s):')
        for guild in self.guilds:
            print(f'\t>{guild.name}(id: {guild.id})')

    def load_cogs(self):
        self.ext.clear()
        print('Loading cogs\n')
        for folder in os.listdir(path='./cogs'):
            print(folder)
            for file in os.listdir(path=f'./cogs/{folder}'):
                print(f'\t{file}')
                if file.endswith('.py'):
                    # The class should not know about extensions when loading, unloading
                    if file[:-3] != "reworkCogWork":
                        self.ext.append(f'cogs.{folder}.{file[:-3]}')
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
