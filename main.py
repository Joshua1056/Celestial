import disnake
from disnake.ext import commands
bot = commands.Bot()
token = "MTIwNTczNDA4MTM2MzU3ODk0MQ.G09iTC.aXzy2HyeeS7L1IdKMehgauTY3seIo7VBb1hjNM"

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready.")
    
@bot.slash_command(name="ping", description="Check bot latency")
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.response.send_message(f"Pong! Heres my latency: {latency}ms")
    
@bot.slash_command(name="support", description="Link to support server")
async def support(ctx):
    await ctx.response.send_message("discord.gg/bvmgjtjjGM")
    
bot.run(token)
