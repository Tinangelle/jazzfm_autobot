import discord
import asyncio
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
TARGET_USER_ID = int(os.getenv("TARGET_USER_ID"))
TARGET_VOICE_CHANNEL_ID = int(os.getenv("TARGET_VOICE_CHANNEL_ID"))
TARGET_TEXT_CHANNEL_ID = int(os.getenv("TARGET_TEXT_CHANNEL_ID"))

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot 已上线：{client.user}')

@client.event
async def on_voice_state_update(member, before, after):
    if member.id == TARGET_USER_ID:
        if after.channel and after.channel.id == TARGET_VOICE_CHANNEL_ID:
            text_channel = client.get_channel(TARGET_TEXT_CHANNEL_ID)
            if text_channel:
                await text_channel.send("m!join")
                await asyncio.sleep(1.5)
                await text_channel.send("m!play http://jazzfm91.streamb.live/SB00009")
                print("已发送 join 和播放命令。")

client.run(TOKEN)