import logging
import discord

from discord.ext import commands
from database import userCollection

# Configure the logger
logging.basicConfig(level=logging.ERROR, filename='bot_errors.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('my_bot')

# create bot
intents = discord.Intents.all()
intents.members = True
intents.messages = True
bot = commands.Bot(command_prefix='$', case_insensitive=True, intents=intents, description="LingoBot")


# help
bot.remove_command('help')


@bot.command(name='help')
async def help_response(ctx):
    help_dm = f"How to use LingoBot\n" \
              f"Commands used:\n" \


    try:
        await ctx.author.send(help_dm)
        await ctx.send(f"sent DM to {ctx.author.mention}")
    except discord.errors.HTTPException as e:
        logger.error(f"Error sending DM to {ctx.author}: {e}")


# say hello
@bot.command(name='hello', description="say hello to the bot")
async def say_hello(ctx):
    response = f'Hello, {ctx.author.mention}!'
    print('said hello')
    await ctx.send(response)


# check user discord id and name
@bot.command(name="check")
async def check(ctx):
    print(ctx.author.name)
    print(ctx.author.id)
    print(ctx.author.name + " checked")



