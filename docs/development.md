# 簡易股票工具 - 本地開發

本工具是使用 Streamlit 為基礎，在簡單的配置過後，你也可以輕易地加入自己的巧思，創造出一個完全屬於你的簡單股票工具。


+ [簡易股票工具 - 本地開發](#簡易股票工具---本地開發)
    + [環境設定](#環境設定)
    + [有用的網站](#有用的網站)

## 環境設定

通常，開啟一個新的環境是最好的選擇。這會需要以下幾個步驟：

1. 首先，你會需要到終端機 (Terminal)，並且確保你的環境中有 `python3` 和 `pip3` 這兩個指令的（如果沒有的話，建議查看別的教學：如何安裝 Python）。打開後，輸入：

    ```sh
    pip3 install pipenv
    ```
2. 現在我們有了 [`pipenv`](https://pipenv.pypa.io/en/latest/)，請你 cd 到存放這個 project 的資料夾，在我的機器上為：

    ```sh
    cd simple-stock-analyzer
    ```
3. 創建 pipenv 環境之後就大功告成啦：

    ```sh
    pipenv shell
    ```
    
    如果是使用別的環境管理工具的朋友，也可以使用：
    ```py
    pip install -r requirements.txt
    ```




## 有用的網站

+ [Emojipedia](https://emojipedia.org/)