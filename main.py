import disnake
from disnake.ext import commands
bot = commands.Bot()
token = "CLASSIFIED"

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

@bot.command(name='kick', description="(KICK+) Kick a user from the server")
@commands.has_permissions(kick_members=True)  # Replace manage_messages with the desired permission
async def kick(ctx, member: disnake.member, reason=str):
    await member.kick(reason=reason)
    await ctx.response.send_message(f"Kicked {member} for {reason}")

@bot.command(name='ban', description="(BAN+) Ban a user from the server")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: disnake.member, reason=str):
    await member.ban(reason=reason)
    await ctx.response.send_message(f"Kicked {member} for {reason}")
    
bot.run(token)
