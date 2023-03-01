import asyncio
import Config
import openai
from pyrogram import filters, Client

Cosmic = Client(name="OpenaiBot",api_id=Config.api_id,api_hash=Config.api_hash)

async def ai(query):
    openai.api_key = Config.openai_api_key
    completion = openai.Completion.create(engine=Config.model, prompt=query, max_tokens=Config.mxtoken, n=1, stop=None,temperature=0.7)
    result = completion.choices[0].text
    return result

@Cosmic.on_message(filters.command("start") & ~filters.group)
async def main(bot,msg):
    user_send_msg = msg.from_user.id
    await bot.send_message(user_send_msg, f"" '👋 Hello ''!\n\n'
                    'Hii ! My name is Sakura-Yamuchan. \n'
                    'And I am a telegram AI based chat-bot \n\n'
                    'Belongs to OpenAIs GPT-3 family \n'
                    'Im here to help answer any questions you may have about a variety of topics.\n'
                    'Feel free to ask me anything! ☺️\n\n'
                    'MADE BY : Soham Sankpal \n'
                    'Git-Hub Profile : https://github.com/blue0777\n'
                    'Git-Hub Reposotory : \n'
                    'Social Media : https://instagram.com/soham_07778/')
    DEL = await msg.reply(f"Typing🤔.......")
    await asyncio.sleep(3)
    await DEL.delete(10)

@Cosmic.on_message(filters.text & ~filters.group)
async def main(bot, msg):
    user_send_msg = msg.from_user.id
    ques = msg.text
    print(ques)
    Config = await ai(ques)
    await asyncio.sleep(3)
    print(Config)
    test = f"`{Config}`"
    await asyncio.sleep(1)
    await bot.send_message(user_send_msg,test)


Cosmic.run()
