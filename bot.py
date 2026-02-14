import discord
from discord.ext import commands
import os

# LẤY TỪ ENV (KHÔNG DÁN TRỰC TIẾP)
TOKEN = os.getenv("DISCORD_TOKEN")
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID", "0"))

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot đã đăng nhập: {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel is None:
        print("❌ Sai hoặc chưa set WELCOME_CHANNEL_ID")
        return

    embed = discord.Embed(
        title="🎉 Chào mừng!",
        description=f"Xin chào {member.mention}, chào mừng bạn đến **{member.guild.name}** ❤️",
        color=0x00ffcc
    )
    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)

    await channel.send(embed=embed)

bot.run(TOKEN)
