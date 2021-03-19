from settingsClass import JsonShell
from discord.ext import commands


class configuration(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(administrator=True)
    @commands.command(name="prefix")
    async def change_prefix_command(self, ctx, *prefix):
        data = JsonShell('serversPrefixes.json')
        currentPrefix = data.get()
        if len(prefix) > 0:
            currentPrefix[str(ctx.message.guild.id)] = prefix
            data.put(data=currentPrefix)
            data.dump('serverPrefixes.json')
        else:
            await ctx.send(currentPrefix[str(ctx.message.guild.id)])

    @commands.has_permissions(administrator=True)
    @commands.command(name="addRole")
    async def add_role_command(self, ctx, emoji, roleID):
        try:
            JsonClass = JsonShell("serversSettings.json")
            serversData = JsonClass.get()
            serverData = serversData[str(ctx.guild.id)]

            rolesByEmoji = serverData["ROLE_BY_EMOJI"]
            rolesByEmoji.update({str(emoji): roleID})

            serverData["ROLE_BY_EMOJI"] = rolesByEmoji
            serversData[str(ctx.guild.id)] = serverData
            JsonClass.put(serversData)
            JsonClass.dump(JsonClass.filePath)

        except Exception as e:
            await ctx.send(f"{type(e).__name__}, {e}")

    @commands.has_permissions(administrator=True)
    @commands.command(name="rmRole")
    async def rm_role_command(self, ctx, roleID):
        try:
            JsonClass = JsonShell("serversSettings.json")
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
        JsonClass = JsonShell("serversSettings.json")
        serversData = JsonClass.get()
        serverData = serversData[str(ctx.guild.id)]
        rolesByEmoji = serverData["ROLE_BY_EMOJI"]
        await ctx.send(rolesByEmoji)


def setup(client):
    client.add_cog(configuration(client))
