# https://discord.com/api/oauth2/authorize?client_id=761979460344872981&permissions=8&scope=bot
import os

from discord.ext import commands
from service.utils import JsonShell
from cogs.help.onHelpMessage import Help_command
from service.startup import Startup


class ClientBot(commands.Bot):
    def __init__(self, command_prefix, help_command, intents):
        self.non_loaded_ext = list()
        self.non_paged_ext = list()
        commands.Bot.__init__(self, command_prefix=command_prefix, help_command=help_command, description=None, intents=intents)

    async def on_ready(self):
        print(f"\n{self.user} connected to the guild(s):")
        for guild in self.guilds:
            print(f"\t>{guild.name}(id: {guild.id})")

    def load_cogs(self):
        settings = JsonShell(f".\\service\\settings.json").get_data_by_key("extensions")
        self.non_loaded_ext = settings["non_loaded_ext"]
        self.non_paged_ext = settings["non_paged_ext"]

        print("loading cogs")
        for folder in os.listdir(path="./cogs"):
            print(folder)
            for fileName in os.listdir(path=f"./cogs/{folder}"):
                print(f"\t{fileName}")
                if fileName.endswith(".py") or fileName.endswith(".pyw"):
                    if fileName not in self.non_loaded_ext:
                        self.load_extension(f'cogs.{folder}.{fileName[:-3]}')


def main():
    startup = Startup()
    startup.set_intents_default()
    startup.set_intents(
        bans=False,
        dm_messages=False,
        dm_reactions=False,
        dm_typing=False,
        emojis=False,
        guild_messages=True,
        guild_reactions=True,
        guild_typing=False,
        guilds=True,
        integrations=False,
        invites=False,
        members=True,
        messages=True,
        presences=True,
        reactions=True,
        typing=False,
        voice_states=True,
        webhooks=False
    )
    client = ClientBot(command_prefix=startup.load_bot_prefix,
                       help_command=Help_command(),
                       intents=startup.get_intents())

    # Bot start
    try:
        client.load_cogs()
    except Exception as e:
        print(type(e).__name__, e)
    client.run(startup.get_bots_token())


if __name__ == "__main__":
    main()
