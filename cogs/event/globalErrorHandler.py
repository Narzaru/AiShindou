import discord
from discord.ext import commands


class GlobarErrorHandler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # not @has_role
        if isinstance(error, commands.MissingRole):
            embed = discord.Embed(
                title='Ой-ой, ошибочка !',
                description=(f'**<@{ctx.author.id}>, у тебя отсутствует необходимая роль `{error.missing_role}`!**'),
                color=0xff0000
            )
        # not @has_permissions
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='Ой-ой, ошибочка !',
                description=(f'**<@{ctx.author.id}>, прости, но у тебе нужно больше прав.\n~Уаа**'),
                color=0xff0000
            )
        # not @is_owner
        elif isinstance(error, commands.NotOwner):
            embed = discord.Embed(
                title='Ой-ой, ошибочка !',
                description=(f'**<@{ctx.author.id}>, это команда только для создателей.\n~Ня**'),
                color=0xff0000
            )
        # any errors
        elif isinstance(error, commands.CommandError):
            embed = discord.Embed(
                title='Ой-ой, ошибочка !',
                description=(f'**<@{ctx.author.id}>, команда не найдена. Или что-то пошло не так!\n~Ня**'),
                color=0xff0000
            )
        return await ctx.send(embed=embed)


def setup(client):
    client.add_cog(GlobarErrorHandler(client))
