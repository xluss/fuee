# インストールした discord.py を読み込む
import discord
import random  # おみくじで使用
from discord.ext import tasks
from datetime import datetime 


# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'NTUyMTM0NjQ4NTgzNjg0MTM4.XQ0OgA.tnoMy9iEHnXpRdVnNPc1zfRZtPg'
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
        embed.add_field(name="[運勢] ", value=random.choice(('大吉', '中吉','吉', '小吉', '凶', '大凶')), inline=False)
        await message.channel.send(embed=embed)     
        
    elif message.content == "団長":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="brain", description=f"団長の迷言集",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[団長] ", value=random.choice(('しゅんすけと寝落ちもしもしすゆけん','ゆうやぁ！','(´ิ ❥ ´ิ♡)ぶっちゅ。','イリヤの開放準備はできとるけん！', 'JK♪JK♪,','セクハラしてなんぼやろ！','監禁♪監禁♪')), inline=False)
        await message.channel.send(embed=embed)

    elif message.content == "ぶちゅんぱ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="ぶちゅんぱ", description=f"ぶちゅんぱチャレンジ",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[ぶちゅんぱ] ", value=random.choice((' <@!429931195686584320> (´ิ ❥ ´ิ♡)ぶっちゅ。',' <@!524861024218775582> (´ิ ❥ ´ิ♡)ぶっちゅ。',' <@!518518488550342677> (´ิ ❥ ´ิ♡)ぶっちゅ。')), inline=False)
        await message.channel.send(embed=embed)


    if message.author.bot:  # ボットのメッセージをハネる
        return



# クラバトについてのコード
    CHANNEL_ID = 591645505256292420
    CHANNEL_ID1 = 516850566060572672
    CHANNEL_ID2 = 592255251814285334
    if message.content == "同時a":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention} もう一人を待ってください") 

    if message.content == "同時b":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention} 同時凸を開始します") 

    if message.content == "1凸":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention}さんの1凸目です") 

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

    if message.content == "持ち越し":

        channel = client.get_channel(CHANNEL_ID)
        await channel.send(f"{message.author.mention}さんの持ち越しです")   

    if message.content == "1凸LA":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention}さんの1凸目のLAです")

    if message.content == "2凸LA":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention}さんの2凸目のLAです")        

    if message.content == "3凸LA":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"{message.author.mention}さんの3凸目のLAです")  
        
    if message.content == "/1st":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"<@&540501141398749220> ゴブリングレート")
        
    if message.content == "/2nd":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"<@&540501141398749220> ライライ")    

    if message.content == "/3rd":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"<@&540501141398749220> シードレイク") 
        
    if message.content == "/4th":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"<@&540501141398749220> ネプテリオン") 
        
    if message.content == "/5th":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"<@&540501141398749220> カルキノス") 
        
    if message.content == "/助けて":
        
        channel = client.get_channel(CHANNEL_ID1)
        await channel.send(f"<@&540501141398749220> 助けてマリオ！")    
        


# ボスに行きたい人を募集するとき


    if    message.content == "!1st":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await message.channel.send("<@&540501141398749220> 1st bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記

    if    message.content == "!2nd":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await message.channel.send("<@&540501141398749220> 2nd bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記  

    if    message.content == "!3rd":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await message.channel.send("<@&540501141398749220> 3rd bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記  

    if    message.content == "!4th":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await message.channel.send("<@&540501141398749220> 4th bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記      

    if    message.content == "!5th":
        # リアクションアイコンを付けたい
        channel = client.get_channel(CHANNEL_ID2)
        q = await message.channel.send("<@&540501141398749220> 5th bossに行きたい人は意志表明してください")
        [await q.add_reaction(i) for i in ('⭕')]  # for文の内包表記         




# Botの起動とDiscordサーバーへの接続
client.run('NTUyMTM0NjQ4NTgzNjg0MTM4.XQ0OgA.tnoMy9iEHnXpRdVnNPc1zfRZtPg')
