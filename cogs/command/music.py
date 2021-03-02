from discord.ext import commands
import youtube_dl
import os
import discord


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel")
        else:
            channel = ctx.author.voice.channel
            self.voice = await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await self.voice.disconnect()

    @commands.command()
    async def play(self, ctx, url: str):
        voiceChannel = ctx.author.voice.channel
        if voiceChannel is None:
            return
        elif len([member for member in voiceChannel.members if self.client.user.id == member.id]):
            pass
        else:
            self.voice = await voiceChannel.connect()

        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for the current playing music end or use the 'stop' command")
            return
        await ctx.send("Getting everything ready, playing audio soon")
        print("Someone wants to play music let me get that ready for them...")
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, 'song.mp3')
        self.voice.play(discord.FFmpegPCMAudio(source="./song.mp3"))
        self.voice.volume = 100
        self.voice.is_playing()


def setup(client):
    client.add_cog(Music(client))
