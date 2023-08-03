#EveryThing ready to implement the bot in the server
import asyncio
import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
intents.members = True
intents.presences = True
intents.guilds = True


#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(command_prefix='!', intents=intents)

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot

async def setup(bot):
    await bot.add_cog(music_cog(bot))

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='Waiting for the second breakfast'))
    print(f'{bot.user.name} is ready!')
    await bot.add_cog(music_cog(bot))

#start the bot with our token
print(str(os.getenv('bot')))
bot.run(str(os.getenv('bot')))

#add the token to the .env file and then import it here with os.getenv('TOKEN') or something like that
