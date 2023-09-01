import discord
from yt_dlp import YoutubeDL
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.queue = {}
        self.voice_clients = {}
        self.IsPlaying = {}
        self.queue_embed = {}
    
    @commands.command(pass_context = True)
    async def join(self, ctx):
        if (ctx.author.voice):
            guild_id = str(ctx.guild.id)
            self.queue[guild_id] = []
            print(self.queue)

            try:
                self.IsPlaying[guild_id] = False
                channel = ctx.author.voice.channel
                await channel.connect()
                self.voice_clients[guild_id] = ctx.voice_client
                await ctx.send("Successfully Connected to a voice channel!")
            except:
                await ctx.send("Already connected to a voice channel!")

    @commands.command(pass_context = True)
    async def leave(self, ctx):
        guild_id = str(ctx.guild.id)

        if (ctx.voice_client):
            self.IsPlaying[guild_id] = False
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I disconnected from the voice channel!")
        else:
            await ctx.send("I'm not in a voice channel! :joy: Gimana sih rek.")
    
    @commands.command()
    async def play(self, ctx, *,music_link: str=None):
        guild_id = str(ctx.guild.id)
        if self.voice_clients[guild_id]:
            if music_link == None:
                await ctx.send("Please put a valid youtube link in the argument!")  
                return   
            
            self.voice_clients[guild_id] = ctx.voice_client
            self.queue_embed[guild_id] = discord.Embed(
                title="Queue",
                description="",
                colour=discord.Colour.red()
            )

            yt_dlp_opts = {'format': 'bestaudio/best',
            'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
            'quiet': True,
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
            }
            ffmpeg_options = {'before_options':
            '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -probesize 200M',
            'options': '-vn'
            }
            
            with YoutubeDL(yt_dlp_opts) as ydl:
                try:
                    info = ydl.extract_info(music_link, download=False)
                    title = info.get("title", None)
                    url2 = info['url']


                except:
                    info = ydl.extract_info(f"ytsearch: {music_link}", download=False)['entries'][0]
                    title = info.get("title", None)
                    url2 = info['url']

                    if len(self.queue[guild_id]) == 0:
                        source = discord.FFmpegPCMAudio(url2, **ffmpeg_options, executable="C:\\ffmpeg\\ffmpeg.exe")
                        vc = self.voice_clients[guild_id]
                        vc.play(source)
                        self.queue[guild_id].append(title)
                        for i in range(0, len(self.queue[guild_id])):
                            self.queue_embed[guild_id].description += str(i+1)+". "+ self.queue[guild_id][i] + f" - added by {ctx.message.author}\n"
                    
                        await ctx.send(embed=self.queue_embed[guild_id])
                        await ctx.send(f"**{title}** is now playing!")
                    else:
                        self.queue[guild_id].append(title)
                        for i in range(0, len(self.queue[guild_id])):
                                self.queue_embed[guild_id].description += str(i+1)+". "+ self.queue[guild_id][i] + f" - added by {ctx.message.author}\n"
                                
                        await ctx.send(embed=self.queue_embed[guild_id])
                        await ctx.send("Added to queue!")
                else:
                    if len(self.queue[guild_id]) == 0:
                        source = discord.FFmpegPCMAudio(url2, **ffmpeg_options, executable="C:\\ffmpeg\\ffmpeg.exe")
                        vc = self.voice_clients[guild_id]
                        vc.play(source)
                        self.queue[guild_id].append(title)
                        for i in range(0, len(self.queue[guild_id])):
                            self.queue_embed[guild_id].description += str(i+1)+". "+ self.queue[guild_id][i] + f" - added by {ctx.message.author}\n"
                    
                        await ctx.send(embed=self.queue_embed[guild_id])
                        await ctx.send(f"**{title}** is now playing!")
                    else:
                        self.queue[guild_id].append(title)
                        for i in range(0, len(self.queue[guild_id])):
                                self.queue_embed[guild_id].description += str(i+1)+". "+ self.queue[guild_id][i] + f" - added by {ctx.message.author}\n"
                                
                        await ctx.send(embed=self.queue_embed[guild_id])
                        await ctx.send("Added to queue!")
        

        else:
            await ctx.send("I'm not in a voice channel! Use ?join while you are in a voice channel, so I can connect to the voice channel.")
    

    @commands.command()
    async def stop(self, ctx):
        guild_id = str(ctx.guild.id)

        if self.voice_clients[guild_id]:
                try:
                    self.voice_clients[guild_id].stop()
                    self.IsPlaying[guild_id] = False
                    self.queue[guild_id].pop(0)
                    self.queue_embed[guild_id].description = ""

                    for i in range(0, len(self.queue[guild_id])):
                        self.queue_embed[guild_id].description += str(i+1)+". "+ self.queue[guild_id][i] + f" - added by {ctx.message.author}\n"
                            
                    await ctx.send(embed=self.queue_embed[guild_id])
                    await ctx.send("Song removed from the queue!")
                except:
                    await ctx.send("No song is currently playing!")

        else:
            await ctx.send("I'm not in a voice channel :joy:! Gimana sih rek.")

    @commands.command()
    async def pause(self, ctx):
        guild_id = str(ctx.guild.id)

        if self.voice_clients[guild_id]:
            self.voice_clients[guild_id].pause()
            await ctx.send("Song is paused!")

    @commands.command()
    async def resume(self, ctx):
        guild_id = str(ctx.guild.id)

        if self.voice_clients[guild_id]:
            self.voice_clients[guild_id].resume()
            await ctx.send("Song is now playing!")


    




async def setup(bot):
    await bot.add_cog(Music(bot))