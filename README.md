<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>README</title>
  <link rel="stylesheet" href="https://stackedit.io/style.css" />
</head>

<body class="stackedit">
  <div class="stackedit__html"><h1 id="threadconnector">ThreadConnector</h1>
<p><img src="https://github.com/r-1317/ThreadConnector/blob/main/images/img01.png?raw=true" alt="ThreadConnector"></p>
<h2 id="概要">概要</h2>
<p>電子掲示板の複数partに別れたスレッドを結合し、datとhtmlで保存します。</p>
<h3 id="出力の例">出力の例</h3>
<p><img src="https://github.com/r-1317/ThreadConnector/blob/main/images/img06.png?raw=true" alt="使用例"><br>
<a href="https://github.com/r-1317/ThreadConnector/blob/main/sample/sample.html">https://github.com/r-1317/ThreadConnector/blob/main/sample/sample.html</a><br>
Githup Pagesを使うと文字化けしたため、一度ダウンロードしてからローカル環境で開いてください。</p>
<h2 id="ダウンロード">ダウンロード</h2>
<p>以下のリンクよりダウンロードできます。</p>
<ul>
<li>
<p><a href="https://github.com/r-1317/ThreadConnector/releases/download/Version1.1/ThreadConnector-1.1.exe">Windows用実行ファイル</a></p>
</li>
<li>
<p><a href="https://github.com/r-1317/ThreadConnector/releases/download/Version1.1/ThreadConnector-1.1">Linux用実行ファイル</a></p>
</li>
<li>
<p><a href="https://github.com/r-1317/ThreadConnector/releases/download/Version1.1/ThreadConnector-1.1.py">ソースファイル</a></p>
</li>
</ul>
<h2 id="使い方">使い方</h2>
<p><img src="https://github.com/r-1317/ThreadConnector/blob/main/images/img01.png?raw=true" alt="使用例"><br>
以下のようなコマンドを入力</p>
<pre><code>.\ThreadConnector-1.1.exe [最新スレッドのURL] [Part数] -f [出力ファイル名] -t [dat取得の間隔(秒) デフォルト1]
</code></pre>
<h3 id="オプション">オプション</h3>
<ul>
<li>
<p><code>-f</code>, <code>--filename</code><br>
保存する際のファイル名です。指定しない場合はデフォルトのファイル名になります。</p>
</li>
<li>
<p><code>-t</code>, <code>--time</code><br>
datを取得するときの待機時間です。<br>
指定しない場合は1秒になり、0.5秒未満を指定すると0.5秒になります。</p>
</li>
</ul>
<h3 id="問題が発生した場合">問題が発生した場合</h3>
<p><img src="https://github.com/r-1317/ThreadConnector/blob/main/images/img02.png?raw=true" alt="問題"><br>
画像にように、<br>
<code>Part〇〇のurlを入力してください。</code><br>
と表示されることがあります。<br>
その時は、検索エンジン等で当該スレッドを探し、URLを入力してください。</p>
<p><img src="https://github.com/r-1317/ThreadConnector/blob/main/images/img08.png?raw=true" alt="無限にURLの入力を求められる"><br>
稀に、正しいURLを入力しても、無限にURLの入力を求められる場合があります。<br>
その時はプログラムを強制終了してください。</p>
<h3 id="正しく動作しないスレッド">正しく動作しないスレッド</h3>
<p><img src="https://github.com/r-1317/ThreadConnector/blob/main/images/img05.png?raw=true" alt="正しく動作しないスレッド"><br>
<a href="https://mao.5ch.net/test/read.cgi/linux/1566402890/">https://mao.5ch.net/test/read.cgi/linux/1566402890/</a><br>
このように、前スレの候補が複数あり、それらが昇順で並んでいる場合は正しく動作しません。<br>
この例では、Part28をPart30として取得してしまいます。</p>
<h2 id="使用しているモジュール">使用しているモジュール</h2>
<p>このソフトウェアは、Pythonを使用しています。</p>
<ul>
<li>Python (<a href="https://docs.python.org/ja/3/license.html#psf-license">Python Software Foundation License</a>) Copyright © 2001-2023 Python Software Foundation. All rights reserved.</li>
</ul>
<p>また、以下のモジュールも使用しています。</p>
<ul>
<li>
<p>requests (<a href="https://www.apache.org/licenses/LICENSE-2.0">Apache License 2.0</a>) Copyright 2019 Kenneth Reitz</p>
</li>
<li>
<p>Python標準ライブラリ (os, time, re, argparse) (<a href="https://docs.python.org/ja/3/license.html#psf-license">Python Software Foundation License</a>) Copyright © 2001-2023 Python Software Foundation. All rights reserved.</p>
</li>
</ul>
<h2 id="ライセンス">ライセンス</h2>
<p>このソフトウェアは、MITライセンスを適用しています。<a href="https://github.com/r-1317/ThreadConnector/blob/main/LICENSE.txt">LICENSE.txt</a>をご確認ください。</p>
</div>
</body>

</html>
