# ThreadConnector
![ThreadConnector](https://github.com/r-1317/ThreadConnector/blob/main/images/img01.png?raw=true)
## 概要

電子掲示板の複数partに別れたスレッドを結合し、datとhtmlで保存します。
### 出力の例
![使用例](https://github.com/r-1317/ThreadConnector/blob/main/images/img06.png?raw=true)
https://github.com/r-1317/ThreadConnector/blob/main/sample/sample.html
Githup Pagesを使うと文字化けしたため、一度ダウンロードしてからローカル環境で開いてください。

## ダウンロード
以下のリンクよりダウンロードできます。
 - [Windows用実行ファイル](https://github.com/r-1317/ThreadConnector/releases/download/Version1.1/ThreadConnector-1.1.exe)
 
 - [Linux用実行ファイル](https://github.com/r-1317/ThreadConnector/releases/download/Version1.1/ThreadConnector-1.1)
 
 - [ソースファイル](https://github.com/r-1317/ThreadConnector/releases/download/Version1.1/ThreadConnector-1.1.py)
 ## 使い方
 ![使用例](https://github.com/r-1317/ThreadConnector/blob/main/images/img01.png?raw=true)
以下のようなコマンドを入力

    .\ThreadConnector-1.1.exe [最新スレッドのURL] [Part数] -f [出力ファイル名] -t [dat取得の間隔(秒) デフォルト1]
   
   ### オプション

 - `-f`, `--filename`
 保存する際のファイル名です。指定しない場合はデフォルトのファイル名になります。
 

 - `-t`, `--time`
 datを取得するときの待機時間です。
 指定しない場合は1秒になり、0.5秒未満を指定すると0.5秒になります。

### 問題が発生した場合
![問題](https://github.com/r-1317/ThreadConnector/blob/main/images/img02.png?raw=true)
画像にように、
`Part〇〇のurlを入力してください。`
と表示されることがあります。
その時は、検索エンジン等で当該スレッドを探し、URLを入力してください。

![無限にURLの入力を求められる](https://github.com/r-1317/ThreadConnector/blob/main/images/img08.png?raw=true)
稀に、正しいURLを入力しても、無限にURLの入力を求められる場合があります。
その時はプログラムを強制終了してください。

### 正しく動作しないスレッド
![正しく動作しないスレッド](https://github.com/r-1317/ThreadConnector/blob/main/images/img05.png?raw=true)
https://mao.5ch.net/test/read.cgi/linux/1566402890/
このように、前スレの候補が複数あり、それらが昇順で並んでいる場合は正しく動作しません。
この例では、Part28をPart30として取得してしまいます。

## 使用しているモジュールなど
このソフトウェアは、Pythonを使用しています。
- Python ([Python Software Foundation License](https://docs.python.org/ja/3/license.html#psf-license)) Copyright © 2001-2023 Python Software Foundation. All rights reserved.

また、以下のモジュールも使用しています。

 - requests ([Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)) Copyright 2019 Kenneth Reitz
 
- os, time, re, argparse ([Python Software Foundation License](https://docs.python.org/ja/3/license.html#psf-license)) Copyright © 2001-2023 Python Software Foundation. All rights reserved.

## ライセンス
このソフトウェアは、MITライセンスを適用しています。[LICENSE.txt](https://github.com/r-1317/ThreadConnector/blob/main/LICENSE.txt)をご確認ください。
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExOTM3NzkyNzddfQ==
-->