<h1>CREATE A DISCORD SERVER</h1>
<ol>
<li>Go to Discord</li>
<li>Create a server with any name</li>
</ol>
<h1>CREATE AN APP</h1>
<ol>
<li>Go to Discord Developer Portal</li>
<li>Create an app with any name.</li>
<li>Now check all the intents.</li>
<li>Go to Oauth2 and generate a token and save it</li>
<li>Check all the text part in the Bot</li>
</ol>
<h1>SENDING A MESSAGE INSIDE THE DISCORD BOT</h1>

```bazaar
import discord
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('token')
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        channel = message.channel
        await channel.send('Hello there')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token=token)

```
<br/>
Now we can add the OPENAI part. In this we are using the gpt 3.5 model.
"# discord-bot" 
