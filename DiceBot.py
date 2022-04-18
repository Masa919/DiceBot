# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'OTY1NTEwNzE4MTgwOTY2NDAw.Yl0P7Q.JssAqcfefhlOERu_6nLevXN1XxY'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    elif 'd' in message.content:
        palam_list = message.content.split(sep='d',maxsplit = 1)
        
        
        if palam_list[0].isdecimal() and palam_list[1].isdecimal():
            palam0 = int(palam_list[0])
            palam1 = int(palam_list[1])
            num = [0] * palam0
            print("dice num :" + str(palam0))
            print("dice range is :" + str(palam1))
            if 0 < palam0 <10:
                for i in range(palam0):
                    num[i] = random.randint(1,palam1)
                reply = f'>{message.author.mention} \nDiceBot:('+ str(palam0)+'D'+ str(palam1) + ')>' + str(num)  
                await message.channel.send(reply)
            else :
                print("number of dice is too many")
                return
        else:
            return
    else:
        return
#     「/neko」と発言したら「にゃーん」が返る処理
#    if message.content == '/neko':
#        await message.channel.send('にゃーん')


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)