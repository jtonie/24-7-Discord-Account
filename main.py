# Made by Shroom#0187 at Discord
# My Github: https://github.com/jtonie
# My Website: https://jtonie.github.com


import discord
import os
import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix=':', self_bot=True, help_command=None)

async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("yourstatus"))

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)

# Never share your Discord Token to anyone unless you want your Discord account to be hacked.
