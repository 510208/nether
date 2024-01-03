---
id: basic_config
title: 基本選項
sidebar_label: 基本選項
sidebar_position: 1
---

# 設定伺服器資訊

在這一章節，你會開始設定基本的伺服器資訊。

## 設定Java版伺服器資訊

首先，一樣打開設定檔，之後我就這樣叫 `config.json` 這個檔案了喔！

打開後請切換到這一段，它應該在檔案的第三行附近：

```json title=config.json
"java-server": {
    "opened": true,
    "mc-server-name": "(Required)",
    "mc-server-ip": "(Required)",
    "mc-server-port": 25565,
    "mc-server-version": "(Required)",
    "mc-server-motd": "(Required)"
},
```

不要去動鍵值對和縮排，我先來說明一下這些選項是啥。

**小提醒！**內容寫 `(Required)` 代表這個是很重要的東西，一定要配置喔！

| 項目(斜體代表可選) | 說明 |
|---|---|
| opened | 是否有Java版伺服器，沒有請填 `false` 、有就填 `true` ，注意都要是小寫喔！ |
| mc-server-name | 伺服器的名稱，這裡直接填就好 |
| mc-server-ip | 伺服器的位址，網址或IPv4都可以，但如果寫IPv4必須確定可以用它連上去 |
| mc-server-port | 伺服器的端口，如果你的伺服器是自己架的，直接填預設25565不用改它，否則請把它改成網址冒號後面的數字 |
| mc-server-version | 遊戲版本，你可以使用 `1.20.1` 或是 `Paper 1.20.1` '兩種格式都可以 |
| *mc-server-motd* | 伺服器的介紹，`server.proptiles` 檔案裡有相應的設定欄位，直接複製過來即可，可以保存原本的json格式 |

## 設定基岩版伺服器資訊

基岩版要設定的項目比較多(打這三個字還要選字夠麻煩的，之後我簡稱成BE喔！)，切到Java底下的設定位置，他大概在

```json title=config.json
"bedrock-server": {
    "opened": true,
    "mc-server-name": "(Required)",
    "mc-server-ip": "(Required)",
    "mc-server-port": 57034,
    "mc-server-is-realm": false,
    "mc-server-realm-uri": "(If switched mc-server-is-realm to true, This is Required)",
    "mc-server-latested": true,
    "mc-server-version": "(If switched mc-server-is-realm to false,This is Required)",
    "mc-server-motd": "(Required)"
},
```

| 項目(斜體代表可選) | 說明 |
|---|---|
| opened | 是否有BE版伺服器，沒有請填 `false` 、有就填 `true` ，注意都要是小寫喔！ |
| mc-server-name | 伺服器的名稱，這裡直接填就好 |
| mc-server-ip | 伺服器的位址，網址或IPv4都可以，但如果寫IPv4必須確定可以用它連上去 |
| mc-server-port | 伺服器的端口，如果你的伺服器是自己架的，直接填預設57034不用改它，否則請把它改成網址冒號後面的數字 |
| mc-server-is-realm | 如果你是租用官方的Realm伺服器，請把這項改成 `true` ，否則保持原本 `false` 不要動 |
| *mc-server-realm-uri* | 如果你上一個項目(mc-server-is-realm)設定 `true`就把這裡改成官方提供的加入Realm連結。它應該長這樣： `https://realms.gg/(十一位數的邀請代碼)` |
| mc-server-latested | 伺服器版本是不是最新，一般都是所以請不用改。如果你 `mc-server-is-realm` 設為true這裡會直接被視為true |
| *mc-server-version* | 基岩版版本，一般建議不用改它 |
| *mc-server-motd* | 伺服器的介紹，`server.proptiles` 檔案裡有相應的設定欄位，直接複製過來即可，可以保存原本的json格式 |

## 配置完成！

到這裡，我想你的配置應該完成了。

恭喜你！隨時想啟動機器人，直接執行 `main.py`