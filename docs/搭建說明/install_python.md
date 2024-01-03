---
id: install_python
title: 安裝 Python
sidebar_label: 安裝 Python
sidebar_position: 1
---

# 開始安裝Python

就如同開始時我說的一樣，但你的電腦裡應該不會內建有Python。這就是我為甚麼會寫這段的原因...

## 對於Windows與其相容系統

Microsoft Windows是一款著名的作業系統，相信介紹不用我多說...

對於Windows(這裡使用的是Windows 10)，預設並沒有內建Python環境，因此我們會需要前往下載。

[前往下載Python 3.10](https://www.python.org/downloads/release/python-3111/)

___

![install_page_guide](https://img.onl/8sboPC)

上面是Python官網提供的下載選項，如果你的電腦跟我一樣是Win10，請選擇 `Windows installer (64-bit)` 選項，這是給64位元的作業系統的，如果你不知道你是不是使用64Bit作業系統，建議你安裝 `Windows installer (32 -bit)` ，相容性會比較好。

下載下來後，請打開該安裝檔。安裝的過程需要系統管理員帳號，請先準備好。

![installer_file](https://img.onl/tUebct)

這是我下載的檔案，我想你應該也是長這樣。

點藍色的文字連結打開安裝檔，你應該會看到這樣的介面：

![install_main](https://img.onl/A0A0T)

請勾選底下的 `Add python.exe to PATH` ，對未來的設定會比較方便。

再來直接點最上面的 `Install Now` ，等一下

![installing_ui](https://img.onl/I2uQwX)

看到這個頁面代表還在安裝。要有耐心。

![install_done](https://img.onl/5O6ioS)

等到這樣，已經很完美了！這代表你的Python應該準備好了，也就是我們可以開始下一步。按下Close關掉這個頁面，因為我們不會需要這個檔案了。

燒等，在那之前，做完都先驗證是否成功是一件很重要的事情！因此，請讓我們按下 `Windows+R` 鍵，輸入 `cmd` 之後按下Enter鍵。

跳出來的黑底介面叫做Cmd，是Command line的縮寫，又稱命令提示字元。

不用去了解它是啥，讓我們輸入以下指令，確認你的Python正常沒有？

```shell
python --version
```

如果你出現這樣的畫面，代表一切都很完美：

```shell
C:\Users\(username)>python --version
Python 3.11.1
```