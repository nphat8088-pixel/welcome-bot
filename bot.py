import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot đã online: {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1472154096566800477)  # thay ID kênh welcome
    if channel:
        await channel.send(f"Chào mừng {member.mention} vào server 🎉")

KHÔNG DÁN TOKEN Ở ĐÂY
bot.run(os.getenv("TOKEN"))