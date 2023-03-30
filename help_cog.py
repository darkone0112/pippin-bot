import discord # pip install discord.py
from discord.ext import commands
#Not implemented in the final build of the bot, but this is the code for the help command nad can be added to the bot by adding it to the cog list in the main file there is no need at the time
#cause of the restrictions of discord bots and the fact that the bot cannot be added to public servers any more
class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """"
        '''
        // Commands:
        /help - Shows this message
        /play - Plays a song from a url or search query (searches youtube)
        /pause - Pauses the current song
        /resume - Resumes the current song
        /skip - Skips the current song
        /queue - Shows the current queue
        /clear - Stops the bot and clears the queue
        '''
        """
        self.text_channel_text = []
    
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                if channel.name == 'pippin-bot':
                    self.text_channel_text.append(channel)
                    await channel.send(self.help_message)
                    
    @commands.command(name = 'help', help = 'Shows this message', aliases = ['h'])
    async def help(self, ctx):
        await ctx.send(self.help_message)
        
        