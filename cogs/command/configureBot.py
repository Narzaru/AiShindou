from settingsClass import JsonShell
from discord.ext import commands


class configuration(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.voice = None

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def prefix(self, ctx, *prefix):
        data = JsonShell('serversPrefixes.json')
        currentPrefix = data.get()
        if len(prefix) > 0:
            currentPrefix[str(ctx.message.guild.id)] = prefix
            data.put(data=currentPrefix)
            data.dump('serverPrefixes.json')
        else:
            await ctx.send(currentPrefix[str(ctx.message.guild.id)])


def setup(client):
    client.add_cog(configuration(client))
