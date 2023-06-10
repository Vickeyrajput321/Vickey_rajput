from .. import bot,openai_key
from telethon import events
import asyncio
import openai

openai.my_api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
  await event.reply("Hello!")
 
  
  
  
  
@bot.on(events.NewMessage(incoming = True,pattern="/get"))
async def start(event):
  await event.reply("Hello This is get  command")
  
  
  await asyncio.sleep(3)
  await a.edit("This is edited msg")
   
   
@bot.on(events.NewMessage(incoming=True, pattern="/Evel"))
async def start(event):
  await event.reply("Hello This is evel command")