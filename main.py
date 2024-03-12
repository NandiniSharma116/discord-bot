import discord
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
token = os.getenv('token')
gptClient = OpenAI(api_key=os.getenv('apiKey'))
chat = ""

def GPTReply(message):
    response = gptClient.chat.completions.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        chat = chat + f"{message.author}: {message.content}"
        if self.user != message.author:
            if self.user in message.mentions:
                channel = message.channel
                prompt = f"{chat}\nAIService: "
                messageToSend = GPTReply(prompt)
                await channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token=token)
