import discord # pip install discord.py
from discord.ext import commands
import os
import youtube_dl # pip install youtube_dl
from help_cog import help_cog # Path: help_cog.py
from music_cog import music_cog # Path: music_cog.py

bot = commands.Bot(command_prefix='sing', description='A bot that plays music')

bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))
bot.remove_command('help')
bot.run(os.getenv('TOKEN'))