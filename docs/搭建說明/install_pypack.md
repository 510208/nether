---
id: install_py_pack
title: 安裝Python套件  
sidebar_label: 安裝Python套件
sidebar_position: 3
---

# 安裝Python套件

剛舖梗了這麼久，就是為了現在

現在我們要開始安裝的，是在Python叫做 **套件(Pack)** 的東西。它提供了更強大的東西，簡單說就是一個很強的函式庫。

首先請你先打開目錄底下的 `requirements.txt` 檔案，內容應該長這樣或是比這多：

```ini title="requirements.txt"
pycord==1.7.3
requests==2.28.1
```

執行以下指令即可開始安裝必須的框架：

```bash
pip install -r requirements.txt
```

然後就完成了，就這麼簡單！

## 找不到套件

有時候(真的機率很低)，程式會找不到Pycord。這時請重新打開你的Cmd，執行以下指令替換掉Pycord檔案：

```bash
py -3 -m pip install -U py-cord
```

這樣再重新啟動一次軟體，應該就完成了！