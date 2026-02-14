import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1472154096566800477)
    if channel:
        await channel.send(f"👋 Chào mừng {member.mention} đến với server!")


bot.run(TOKEN)

