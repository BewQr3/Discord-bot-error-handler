import discord
from discord.ext import commands
#import required modules

bot = commands.Bot(command_prefix='t!')
#makes bots prefix = t!

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
#random stuff

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
        error = discord.Embed(title='**Missing args! ERROR 001**', description=':fire: :fire: Missing argument!', color=0x3b1261)
        await bot.send_message(ctx.message.channel, embed=error)
        print("Error 001 occured in {} at {} by {} ".format(ctx.message.server,ctx.message.channel, ctx.message.author))
    if isinstance(error, discord.ext.commands.errors.CommandOnCooldown):
        error = discord.Embed(title='**Command on cooldown! ERROR 002**', description='command is on cooldown bro ;)', color=0x3b1261)
        await bot.send_message(ctx.message.channel, embed=error)
        print("Error 002 occured in {} at {} by {} ".format(ctx.message.server, ctx.message.channel, ctx.message.author))

@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user) # a command with cooldown so we can test this code
async def cooldown(ctx):
    await bot.say(":ok_hand: Working!")

@bot.command(pass_context=True) #another command to test required args error
async def avatar(ctx, user: discord.Member) :
    await bot.say(user.avatar_url)

bot.run('Replace this text with your token..') #replace that with your bot's token

#hope that worked , and enjoy ;)
