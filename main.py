import disnake
from disnake.ext import commands
bot = commands.Bot()
token = "you thought i left the token here? of course not!"

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
