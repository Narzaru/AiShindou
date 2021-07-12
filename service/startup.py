import os
import discord
from dotenv import load_dotenv
from service.utils import JsonShell
from service.sql import sqlite, Factory


class Startup():
    def __init__(self):
        load_dotenv()
        self.__intents = None
        self.load_settings()

    async def load_bot_prefix(self, client, message):
        db = sqlite(r"service\discordBot.db")
        prefixes = db.select(
            columns_name="prefix",
            table_name="prefixes",
            filter=f"guildID == {message.guild.id}",
            factory=Factory().string_factory
        )
        return prefixes

    def load_settings(self):
        data = JsonShell("cogs\\service\\serversPrefixes.json")
        self.not_extensions = data

    def set_none_intents(self):
        self.__intents = discord.Intents.none()
        return self

    def set_all_intents(self):
        self.__intents = discord.Intents.all()
        return self

    def set_intents_default(self):
        self.__intents = discord.Intents.default()
        return self

    def set_intent(self, key, value):
        if self.__intents is None:
            print(f"[WARNING] intents not installed, it will be installed by default")
            self.set_intents_default()
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

    def get_bots_token(self):
        return os.getenv("DISCORD_TOKEN")
