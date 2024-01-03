---
id: install_pack
title: 安裝套件  
sidebar_label: 安裝套件
sidebar_position: 2
---

# 安裝套件

在你的Python安裝好後，請前往官網下載Nether(拖了一個說明的時間，總算要下載主程式了...)

[點這裡前往官網](https://github.com/510208/nether)

這是專案的原始碼頁面，請點右上角綠色的 `< >Code` ，點擊 `Download Zip`

![gh_page_fm_downloader](https://img.onl/9vj1Fw)

完美！現在你會得到一個Zip壓縮包，這就是主程式，真的很小

```tree
C:.
├── .gitignore
├── config.json
├── LICENSE
├── main.py
├── requirements.txt
└── README.md
```

讓我來說明一下裡面的東西要幹嘛？

- **.gitignore**：Git所需使用的檔案，這大概不關你的事
- **config.json**：主程式配置文件，等等會叫你改的大部分都是這個
- **main.py**：主程式，如果文件沒說要改，請你別改吧...
- **requirements.txt**：需求檔案，這寫了這套軟體的所有需要模組，下一回會告訴你怎麼用它
- **README.md**：這是軟體的說明文件，看你要不要留

~~也就是說，軟體真的有用的只有 `config.json` 和 `main.py` 而已...~~