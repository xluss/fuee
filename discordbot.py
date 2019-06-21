# インストールした discord.py を読み込む
import discord
import random  # おみくじで使用
from discord.ext import tasks
from datetime import datetime 


# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTg0Mzk2NTUwOTIzNDg1MjAw.XQuybw.sqdcDjrLsceGTvjJQF1Le36qqPk'
# 接続に必要なオブジェクトを生成
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')



# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    
    if message.content == '/obuse':
        await message.channel.send('0:40 クスリ')

        
    elif message.content == "!おみくじ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('大吉', '吉', '凶', '大凶')), inline=False)
        await message.channel.send(embed=embed) 

    elif message.content == "!hori":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="hori", description=f"ほりくんの迷言集",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[hori] ", value=random.choice(('ぬそぉ', 'ちんちんケルベロス', 'ムラムラ')), inline=False)
        await message.channel.send(embed=embed) 

        
    elif message.content == "!brain":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="brain", description=f"ぶれいんさんの迷言集",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[brain] ", value=random.choice(('上ぶれいん', '下ぶれいん', '神ぶれいん', '凶ぶれいん')), inline=False)
        await message.channel.send(embed=embed) 

        
    elif message.content == "!toroy":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="brain", description=f"とろいさんの迷言集",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[toroy] ", value=random.choice(('呼ばれて飛び出てとろいさん', '寝落ちたわ')), inline=False)
        await message.channel.send(embed=embed)

        
    if message.author.bot:  # ボットのメッセージをハネる
        return



# クラバトについてのコード
    CHANNEL_ID = 584441360506028213
    CHANNEL_ID1 = 584440901175214115
    if message.content == "1凸":
        
        channel = client.get_channel(CHANNEL_ID1)
        await message.channel.send(f"{message.author.mention}さんの1凸目です") 

    if message.content == "2凸":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention}さんの2凸目です")    

    if message.content == "3凸":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention}さんの3凸目です")

    if message.content == "1凸終了":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention}さんの1凸目終了です")
        
    if message.content == "2凸終了":
          
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention}さんの2凸目終了です")   

    if message.content == "3凸終了":

        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"本日の{message.author.mention}さんの凸は終了です、お疲れ様でした")   
    
    if message.content == "/LA":
        
        channel = client.get_channel(CHANNEL_ID1)
        await message.channel.send(f"{message.author.mention}さんのLAです")

    if message.content == "/nbs":
        
        channel = client.get_channel(CHANNEL_ID1)
        await message.send(f"<@&584396550923485200> next boss")
        
    if message.content == "/助けて":
        
        channel = client.get_channel(CHANNEL_ID1)
        await message.send(f"<@&584396550923485200> 助けてマリオ！")    
        



# ボスに行きたい人を募集するとき
    CHANNEL_ID2 = 584441021367058435
    if    message.content == "/1st":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await channel.send("1st bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記

    if    message.content == "/2nd":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await channel.send("2nd bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記  

    if    message.content == "/3rd":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await channel.send("3rd bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記  

    if    message.content == "/4th":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await channel.send("4th bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記      

    if    message.content == "/5th":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await channel.send("5th bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記         

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '05:00':
        channel = client.get_channel(560495611280097295)
        await channel.send('プリコネの更新時間だよ～')  

    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '04:00':
        channel = client.get_channel(560495611280097295)
        await channel.send('プリコネの更新1時間前だよ～')  

#ループ処理実行
loop.start()

# Botの起動とDiscordサーバーへの接続
client.run('NTg0Mzk2NTUwOTIzNDg1MjAw.XQuybw.sqdcDjrLsceGTvjJQF1Le36qqPk')
