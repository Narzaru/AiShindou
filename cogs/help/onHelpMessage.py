import discord
from discord.ext import commands
from service.utils import TemplateColours


class Help_command(commands.MinimalHelpCommand):
    async def send_pages(self):
        ctx = self.get_destination()
        self.paginator.suffix = "\nif something is wrong, he is to blame\n ---> <@202011264589758464>"

        for page in self.paginator.pages:
            embed = discord.Embed(description=page, color=TemplateColours("service\\templateColours.json").Yellow)
            await ctx.send(embed=embed)
