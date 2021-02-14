import json
from discord.ext import commands


class ConfigureBot(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def prefix(self, ctx, prefix=None):
        with open('serversPrefixes.json', 'r') as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open('serversPrefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)


def setup(client):
    client.add_cog(ConfigureBot(client))
