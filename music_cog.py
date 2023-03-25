import discord
from ast import alias
from youtube_dl import YoutubeDL
from discord.ext import commands

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
        #all the music related stuff
        self.is_playing = False
        self.is_paused = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = None

     #searching the item on youtube
    def search_yt(self, query):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
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
            self.is_playing = True
            nurl = self.music_queue[0][0]['source']
            
            print("Ojo")
            
            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()
                print("Ojo1")
                
                if self.vc == None:
                    await ctx.send("No se pudo conectar al canal de voz")
                    print("Ojo1.1")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])
                print("Ojo2")
                
            self.music_queue.pop(0)
            print("Ojo3")
            print(nurl + " is playing")
            self.vc.play(discord.FFmpegPCMAudio(nurl, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())        
        else:

            self.is_playing = False
            
    @commands.command(name = 'play', help = 'Plays a song from a url or search query (searches youtube)', alias = ['p',"sing","s","playing"])
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
        if self.is_paused == False:
            self.is_paused = True
            self.is_playing = False
            print(str(self.is_paused) + " " + str(self.is_playing))
            await ctx.send('Song paused')
            self.vc.pause()
        else:
            await ctx.send("No hay canciones reproduciendose")
            
    @commands.command(name = 'resume', help = 'Resumes the current song', aliases = ['r'])
    async def resume(self, ctx, *args):
        if self.is_paused == True and self.is_playing == False:
            self.is_paused = False
            self.is_playing = True
            print(str(self.is_paused) + " " + str(self.is_playing))
            self.vc.resume()
            """ await self.play_music(ctx) """
        else :
            await ctx.send("No hay canciones en pausa")
            
    @commands.command(name = 'skip', help = 'Skips the current song', aliases = ['s'])
    async def skip(self, ctx, *args):
        if self.is_playing:
            print("Skipping song")
            self.vc.stop()

            
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

    @commands.command(name = 'leave', help = 'Stops the bot and clears the queue', aliases = ['l','disconnect','dc', 'ireleaseyoufromyourservitude'])
    async def leave(self, ctx, *args):
        self.music_queue = []
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()
        await ctx.send('GREAT! WHERE ARE WE GOING?')
        