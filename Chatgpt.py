from telethon import events 
from .. import bot
from .. import openai_key
from telethon.tl.custom import Button 
import asyncio
import openai
import telethon

openai_key = "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"

openai.my_api_key = openai_key
model_engine="gpt-3.5-turbo"


k_board = [[Button.inline("stop and reset",b"stop_gpt")]]

@bot.on(events.NewMessage(incoming=True,pattern="(?i)/ask"))
async def _gpt(event):
  sender_id = event.sender_id
  gpt_msg = "Hello! I am Vickey rajput321 Ai that can answer to all queries"
  try:
   await bot.send_message(sender_id, gpt_msg)
   async with bot.conversation(await event.get_chat(), exclusive= True, timeout=600) as conv:
     history= []
     
     while True:
       gpt_msg = "sender Your Question "
       u_input = await send_recieve(gpt_msg,conv, k_board)
       if u_input is None:
         gpt_msg= "conversation reset.Type  /ask to start a new one"
         await bot.send_message(sender_id,gpt_msg)
         break
       else:
         gpt_msg="I got your question wait for response "
         ab= await bot.send_messag(sender_id,chat_gpt)
         history.append({"role":"user","content":u_input})
         c_comp= openai.ChatCompletion.create(model=model_engine,
         messages=history,
         max_tokens=400,
         n=1, 
         temperature=0.1
         )
       response =c_comp.choices[0]. messages. content
       history.append({"role":"assistant",  "convert":response})
       await ab.delete()
       await bot.send_message(sender_id, response,parse_mode="Markdown")
  except asyncio.TimeoutError:
    await bot.send_message(sender_id,"conversation ended due to no response ")
    return 
  except telethon.errors.AlreadyInConversationError:
       pass 
  except Exception as e:
    print (e)
    await bot.send_message(sender_id,"convoended.Something Went Wrong")
    return 
   
 
async def send_recieve(gpt_msg, conv, keyboard ):
  
    msg = await conv.send_message(gpt_msg,  buttons= keyboard)
    done, _ = await asyncio.wait({await conv.wait_event(events.CallbackQuery()),await conv.get_response()}, return_when=asyncio.FIRST_COMPLETED)
    result=done.pop().result()
    await message.delete()

    if isinstance(result, event.CallbackQuery.event):
     return none
    else:
      return result.message.strip()



