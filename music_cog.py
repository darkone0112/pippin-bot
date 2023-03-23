import discord
import youtube_dl
from discord.ext import commands

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.is_playing = False
        self.is_paused = False
        
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        
        self.vc = None

    def search_yt(self, query):
        with youtube_dl.YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                get_info = ydl.extract_info("ytsearch:%s" % query, download=False)['entries'][0]
            except Exception:
                return False
        return {'source': get_info['formats'][0]['url'], 'title': get_info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True
            nurl = self.music_queue[0][0]['source']
            self.music_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(nurl, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    async def play_music(self, ctx):# Play a song from a url or search query (searches youtube) 
        if len(self.music_queue) > 0:
            self.is_playimg = True
            nurl = self.music_queue[0][0]['source']
            
            if self.vc == None:
                await ctx.send('We have no songs for great halls and... evil times')
                return
            else:
                await self.vc.move_to(self.music_queue[0][1])
            
            self.music_queue.pop(0)
            
            self.vc.play(discord.FFmpegPCMAudio(nurl, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
            
        else:
            self.is_playing = False
            
    @commands.command(name = 'play', help = 'Plays a song from a url or search query (searches youtube)', aliases = ['p',"sing","s","playing"])
    async def play(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send('We have no songs for great halls and... evil times')
        elif self.is_paused:
            self.vc.resume()
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send('Song not found')
            else:
                await ctx.send('Song added to queue')
                self.music_queue.append([song, voice_channel])
                
                if self.is_playing == False:
                    await self.play_music(ctx)
                    
    @commands.command(name = 'pause', help = 'Pauses the current song', aliases = ['pa'])
    async def pause(self, ctx, *args):
        if self.is_playing and not self.is_paused:
            self.vc.pause()
            self.is_paused = True
            await ctx.send('Song paused')
        elif self.is_paused:
            self.vc.resume()
            
    @commands.command(name = 'resume', help = 'Resumes the current song', aliases = ['r'])
    async def resume(self, ctx, *args):
        if self.is_paused:
            self.vc.resume()
            self.is_paused = False
            self.is_playing = True
            await self.play_music(ctx)
            
    @commands.command(name = 'skip', help = 'Skips the current song', aliases = ['s'])
    async def skip(self, ctx, *args):
        if self.is_playing:
            self.vc.stop()
            await self.play_music(ctx)
            
    @commands.command(name = 'queue', help = 'Shows the current queue', aliases = ['q'])
    async def queue(self, ctx, *args):
        if len(self.music_queue) > 0:
            await ctx.send('Current queue:')
            for song in self.music_queue:
                await ctx.send(song[0]['title'])
        else:
            await ctx.send('No songs in queue')
            
    @commands.command(name = 'clear', help = 'Stops the bot and clears the queue', aliases = ['cls'])
    async def clear(self, ctx, *args):
        self.music_queue = []
        self.is_playing = False
        self.is_paused = False
        await ctx.send('Queue cleared')

    @commands.command(name = 'leave', help = 'Stops the bot and clears the queue', aliases = ['l','disconnect','dc', 'i release you from your servitude'])
    async def leave(self, ctx, *args):
        self.music_queue = []
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()
        await ctx.send('GREAT! WHERE ARE WE GOING?')
        

        
        
        
        
    
