import discord
import json
import logging
import requests

ICONASCII = """
    .        
    #=          ___   _                    _   ___               ,__   .      ___                      ____           .   
    *::-      .'   `. \ ___    ____ `   ___/ .'   \ .___    ___  /  ` _/_   .'   \   __.  .___    ___  /   \    __.  _/_  
    *-::+     |     | |/   \  (     |  /   | |      /   \  /   ` |__   |    |      .'   \ /   \ .'   ` |,_-<  .'   \  |   
    *  .#     |     | |    `  `--.  | ,'   | |      |   ' |    | |     |    |      |    | |   ' |----' |    ` |    |  |   
    .::.+      `.__.' `___,' \___.' / `___,'  `.__, /     `.__/| |     \__/  `.__,  `._.' /     `.___, `----'  `._.'  \__/
       :.    

==========================================================================================================================
"""

print(ICONASCII)

# 設定 logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

with open('config.json', 'r', encoding='utf8') as jfile:
    config = json.load(jfile)

intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)

# 定義基本常數
SAMHEADERURL = "https://img.onl/Kgrc15"
TOKEN = config["discord-token"]

@bot.slash_command(name="ip", description="顯示伺服器IP")
async def ip(ctx: discord.ApplicationContext):
    # 判斷伺服器是否開啟
    if config["java-server"]["opened"]:
        jeId = config["java-server"]["mc-server-ip"]
        jeVer = config["java-server"]["mc-server-version"]
        if config["java-server"]["mc-server-port"] == "":
            jePort = "19132"
        else:
            jePort = config["bedrock-server"]["mc-server-port"]
    
        jeId = config["java-server"]["mc-server-ip"] + ":" + str(jePort)
    else:
        jeId = "伺服器未開啟"
    
    if config["bedrock-server"]["opened"]:
        # 是否為Realm伺服器
        if config["bedrock-server"]["mc-server-is-realm"]:
            beId = f"Realm伺服器，加入連結為{config['bedrock-server']['mc-server-realm-uri']}"
            beVer = "目前的最新版本"
        else:
            beId = config["bedrock-server"]["mc-server-ip"]
            if config["bedrock-server"]["mc-server-latested"]:
                beVer = "目前的最新版本"
            else:
                beVer = config["bedrock-server"]["mc-server-version"]
        if config["bedrock-server"]["mc-server-port"] == "":
            bePort = "19132"
        else:
            bePort = config["bedrock-server"]["mc-server-port"]
    else:
        beId = "伺服器未開啟"
    
    # 創建一個 Embed 物件
    embed = discord.Embed(title="伺服器資訊", color=0x00ff00)
    embed.add_field(name="Java 伺服器", value=jeId, inline=False)
    embed.add_field(name="Java 版本", value=jeVer, inline=False)
    embed.add_field(name="Bedrock 伺服器", value=beId, inline=False)
    embed.add_field(name="Bedrock 端口", value=bePort, inline=False)
    embed.add_field(name="Bedrock 版本", value=beVer, inline=False)
    embed.set_footer(text="機器人由 SamHacker 設計", icon_url=SAMHEADERURL)

    # 發送 Embed 訊息
    await ctx.respond(embed=embed)

# ======================
# 取得伺服器版本(Beta)
# ======================
@bot.slash_command(name="version", description="顯示伺服器版本")
async def version(ctx: discord.ApplicationContext):
    # 判斷伺服器是否開啟
    if config["java-server"]["opened"]:
        jeVer = config["java-server"]["mc-server-version"]
    else:
        jeVer = "伺服器未開啟"

    if config["bedrock-server"]["opened"]:
        # 是否為Realm伺服器
        if config["bedrock-server"]["mc-server-is-realm"]:
            beVer = "目前的最新版本"
        else:
            if config["bedrock-server"]["mc-server-latested"]:
                beVer = "目前的最新版本"
            else:
                beVer = config["bedrock-server"]["mc-server-version"]
    else:
        beVer = "伺服器未開啟"
    
    # 創建一個 Embed 物件
    embed = discord.Embed(title="伺服器版本", color=0x00ff00)
    embed.add_field(name="Java 版本", value=jeVer, inline=False)
    embed.add_field(name="Bedrock 伺服器", value=beVer, inline=False)
    embed.set_footer(text="機器人由 SamHacker 設計", icon_url=SAMHEADERURL)
    
    # 發送 Embed 訊息
    await ctx.respond(embed=embed)


@bot.slash_command(name="say", description="借刀殺人好方法")
async def global_command(
    ctx: discord.ApplicationContext, message: str
):  # Takes one integer parameter
    await ctx.respond(message)

@bot.slash_command(name="alive", description="機器人的生命到頭沒")
async def alive(ctx: discord.ApplicationContext):
    await ctx.respond("我是機器人，不會死")

@bot.slash_command(name="乒", description="顯示機器人延遲")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"乓！{round(bot.latency * 1000)}ms")

# 系統訊息

@bot.event
async def on_ready():
    print(f"==========\n"*2)
    print(f"Logged in as {bot.user}")
    logging.info(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_message(message):
    # 如果訊息是由 bot 自己發送的，則直接返回
    if message.author == bot.user:
        return

    # 如果訊息提及了 bot，則回覆 "有何貴事"
    if bot.user in message.mentions:
        await message.reply("有何貴事")
    
    # 如果訊息內容包含 "活著嗎"，則回覆 "我是機器人，不會死"
    if "活著嗎" in message.content:
        await message.reply("我是機器人，不會死")

# To learn how to add descriptions and choices to options, check slash_options.py
bot.run(TOKEN)

