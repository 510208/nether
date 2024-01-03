---
id: get_token
title: 取得Discord Bot Token
sidebar_label: 取得Token
sidebar_position: 4
---

# 取得Discord Bot Token

Token是一種身份驗證方式，類似於RestfulAPI，但卻又不完全相似。Token採用一組隨機產生的亂碼作為身份驗證方式，使用這種方法的平台如Discord等。
在此，Discord需要的Token是用以驗證你是否為機器人所有者所需的一個憑據。取得該憑據請照以下方法操作即可。

Discord Bot Token是一串特殊的字串，你可以用這個東西控制你的機器人

:::warning

**請注意!** 禁止將Token提供給其他不信任的人，把它當成你的密碼一樣保管

:::

### 前置工作

* 註冊一個Discord帳號

### 建立Token設定檔

- 前往 [Discord Developer Portal](https://discordapp.com/developers/applications)
- 登入你的Discord帳號（如果還沒的話）
- 點按右上角“New Applaction”
- 幫應用程式命名。
- 點選選單左邊的 Bot 後按 Add Bot（可以幫 Bot 另外命名，也可以幫他上傳頭像。）
- 點擊 Reset Token 並把這個 Token 記錄下來，該Token只會顯示一次請保存好。
- 點選左邊選單的 OAuth2
- 在 Scope 的地方勾選 Bot 並按下 Copy。

將複製下來的網址貼到網址列就可以邀請自己的 Bot 加入自己建立的 Server 囉！

### 配置Nether的檔案

打開 `config.json` ，推薦採用 [Visual Studio Code](https://code.visualstudio.com)編輯該檔案，使用方法請上網路搜尋。

你已完成一大半了！將 `discord-token` 鍵後方的項目改為你的Token，它原本應該長這樣：

```json title=config.json
"discord-token": "ENTER-YOUR-TOKEN-IN-THERE(Required)",
```
把`ENTER-YOUR-TOKEN-IN-THERE(Required)`替換成你的Token，應該像是這樣：

```json title=config.json
"discord-token": "MTILikeSamHacker510208isnakjfirkidjwj2oJkdknwJndjBHhHbU2848",
```

喔對了，上面那串token是假的，我亂打的，不要照抄喔。

:::warning

只要有Token就可以在你的伺服器裡為所欲為，所以你絕對要保護好它！

:::