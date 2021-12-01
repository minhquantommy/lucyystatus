import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os

PREFIX = ("$")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')

@bot.event
async def on_ready():
    activity = discord.Game(name="Circus Is Offline", type=2)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Bot is ready!")
keep_alive()
bot.run('TOKEN')