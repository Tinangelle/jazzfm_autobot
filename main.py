import discord
import os
import requests

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TARGET_CHANNEL_ID = 1394712248634708028
JOCKIE_BOT_ID = 411916947773587456

WEBHOOK_URL = "https://discord.com/api/webhooks/1395432088139730944/S-XiYoNIcpz9d0ywEyvQPkYAYJxhXdBP6ua_mNA_4AehhSlX6bxYrxaWkmmBHOPZ2Df8"

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot 已上线：{client.user}')

@client.event
async def on_voice_state_update(member, before, after):
    if member.id == JOCKIE_BOT_ID:
        if after.channel and after.channel.id == TARGET_CHANNEL_ID:
            print("🎶 Jockie 加入 jazz_fm，准备播放 FM91")
            data = {
                "content": "m!play http://jazzfm91.streamb.live/SB00009",
                "username": "fake33"
            }
            response = requests.post(WEBHOOK_URL, json=data)
            print(f"Webhook 状态码：{response.status_code}")

client.run(TOKEN)