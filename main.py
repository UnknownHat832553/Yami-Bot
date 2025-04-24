import nextcord
from nextcord.ext import commands
import os

from server import server_on

intents = nextcord.Intents.all()
message_to_edit = None
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name="เป็นผู้แลต่างๆ ในเซิร์ฟ"))
    print(f'Bot {bot.user} Now available!')
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and filename != '__init__.py':
        bot.load_extension(f'cogs.{filename[:-3]}')

server_on()
bot.run(os.getenv('TOKEN'))