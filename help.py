import discord
from discord.ext import commands


class Help_command(commands.MinimalHelpCommand):
    async def send_pages(self):
        ctx = self.get_destination()
        for page in self.paginator.pages:
            embed = discord.Embed(description=page)
            await ctx.send(embed=embed)
