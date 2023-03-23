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
    await bot.change_presence(activity=discord.Game(name='Listening to !help'))
    print(f'{bot.user.name} is ready!')
    await bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run("MTA4ODQ4Mzc1Nzc3MTcyMjc3Mg.G5qUqp.rIzFUs9K_tswXU4jqpuOuv-BJG06lI5dS38wtk")