from service.utils import JsonShell, TemplateColours
from discord.ext import commands
from discord import Embed


class configuration(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name="prefix")
    async def change_prefix_command(self, ctx, *prefix):
        data = JsonShell('cogs\\service\\serversPrefixes.json')
        currentPrefixes = data.get()

        if len(prefix) > 0 and ctx.author.guild_permissions.administrator:
            currentPrefixes[str(ctx.message.guild.id)] = prefix
            data.put(data=currentPrefixes)
            data.dump('cogs\\service\\serversPrefixes.json')

        else:
            prefixes = str()

            for prefix in currentPrefixes[str(ctx.message.guild.id)]:
                prefixes += prefix + " "

            embed = Embed(
                title="Здесь я понимаю такие префиксы:",
                description=prefixes,
                color=TemplateColor("cogs\\service\\templateColors.json").Green
            )
            await ctx.send(embed=embed)

    @commands.has_permissions(administrator=True)
    @commands.command(name="addRole")
    async def add_role_command(self, ctx, emoji, roleID):
        try:
            JsonClass = JsonShell("cogs\\service\\serversSettings.json")
            serversData = JsonClass.get()
            serverData = serversData[str(ctx.guild.id)]

            rolesByEmoji = serverData["ROLE_BY_EMOJI"]
            rolesByEmoji.update({str(emoji): roleID})

            serverData["ROLE_BY_EMOJI"] = rolesByEmoji
            serversData[str(ctx.guild.id)] = serverData
            JsonClass.put(serversData)
            JsonClass.dump("cogs\\service\\serversSettings.json")

        except Exception as e:
            await ctx.send(f"{type(e).__name__}, {e}")

    @commands.has_permissions(administrator=True)
    @commands.command(name="rmRole")
    async def rm_role_command(self, ctx, roleID):
        try:
            JsonClass = JsonShell("cogs\\service\\serversSettings.json")
            serversData = JsonClass.get()
            serverData = serversData[str(ctx.guild.id)]

            rolesByEmoji = serverData["ROLE_BY_EMOJI"]
            rolesByEmoji.pop(roleID)

            serverData["ROLE_BY_EMOJI"] = rolesByEmoji
            serversData[str(ctx.guild.id)] = serverData
            JsonClass.put(serversData)
            JsonClass.dump(JsonClass.filePath)

        except Exception as e:
            await ctx.send(f"{type(e).__name__}, {e}")

    @commands.has_permissions(administrator=True)
    @commands.command(name="showRoles")
    async def show_roles_command(self, ctx):
        JsonClass = JsonShell("cogs\\service\\serversSettings.json")
        serversData = JsonClass.get()
        serverData = serversData[str(ctx.guild.id)]
        rolesByEmoji = serverData["ROLE_BY_EMOJI"]
        await ctx.send(rolesByEmoji)


def setup(client):
    client.add_cog(configuration(client))
