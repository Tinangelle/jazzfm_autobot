import discord
import asyncio
import os
import requests

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TARGET_USER_ID = int(os.getenv("TARGET_USER_ID"))
TARGET_VOICE_CHANNEL_ID = int(os.getenv("TARGET_VOICE_CHANNEL_ID"))

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
    if member.id == TARGET_USER_ID:
        if after.channel and after.channel.id == TARGET_VOICE_CHANNEL_ID:
            print("检测到目标用户进入语音频道，发送 Webhook 指令")
            data = {
                "content": "m!play http://jazzfm91.streamb.live/SB00009",
                "username": "fake33"
            }
            response = requests.post(WEBHOOK_URL, json=data)
            print("Webhook 响应状态码：", response.status_code)

client.run(TOKEN)