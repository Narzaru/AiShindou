from discord.ext import commands
# from service.utils import JsonShell
import os


class CogWork(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="test", hidden=True)
    @commands.is_owner()
    async def test_command(self, ctx):
        await ctx.send("oWo это тест чего-то")
        await ctx.send("_")

    @commands.command(name="unload", hidden=True)
    @commands.is_owner()
    async def unload_cogs_command(self, ctx):
        extensions = list(self.client.extensions.items())
        for extension in extensions:
            extension = extension[0]
            if (extension.split(".")[-1] + ".py") not in self.client.non_paged_ext:
                self.client.unload_extension(extension)

    @commands.command(name="load", hidden=True)
    @commands.is_owner()
    async def load_cogs_command(self, ctx):
        print("loading cogs")
        for folder in os.listdir(path="./cogs"):
            print(folder)
            for fileName in os.listdir(path=f"./cogs/{folder}"):
                print(f"\t{fileName}")
                if fileName.endswith(".py") or fileName.endswith(".pyw"):
                    if fileName not in self.client.non_loaded_ext and fileName not in self.client.non_paged_ext:
                        self.client.load_extension(f'cogs.{folder}.{fileName[:-3]}')

    @commands.command(name="reload", hidden=True)
    @commands.is_owner()
    async def reload_cogs_command(self, ctx):
        await self.unload_cogs_command(ctx)
        await self.load_cogs_command(ctx)


def setup(client):
    client.add_cog(CogWork(client))
