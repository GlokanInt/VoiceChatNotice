import discord
import os
from dotenv import load_dotenv

from server import server_thread

# .envファイルの内容を読み込む
load_dotenv()

# TOKENを環境変数から取得する
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
    botRoom = client.get_channel(1228946923491299369)

    # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
    announceChannelIds = [1228944111491612697]

    # 入室通知
    if after.channel is not None and after.channel.id in announceChannelIds:
        # チャンネルに誰もいなかった状態から1人入室したとき（通話開始）
        if before.channel is None and len(after.channel.members) == 1:
            await botRoom.send("**" + after.channel.name + "** で、__" + member.name + "__ が通話を開始しました！")

    # 退室通知
    if before.channel is not None and before.channel.id in announceChannelIds:
        # 退室後にチャンネルのメンバーが0人になったとき（通話終了）
        if len(before.channel.members) == 0:
            await botRoom.send("**" + before.channel.name + "** で、通話が終了しました！")

# Koyeb用 サーバー立ち上げ
server_thread()
# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run(token)
