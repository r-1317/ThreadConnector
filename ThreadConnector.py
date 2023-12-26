import argparse
import os
import requests
import time
import re

output_dir = "" #プログラムと同一ディレクトリに仕様変更

#関数の定義
def default_filename():
  n = 0
  while True:
    fn = f"結合済み({n})"
    # print(output_dir + fn) #デバッグ
    if os.path.isfile(output_dir + fn + ".dat"):
      n += 1
    else:
      return fn
      break

def find_url(dat):
  s = dat.find("前スレ")  #前スレの場所を探す
  dat = dat[s:] #前スレ以前を削除
  pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+" #引用元: https://trelab.info/python/python-%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE%E3%81%A7url%E3%81%AE%E4%B8%80%E8%87%B4%E3%83%81%E3%82%A7%E3%83%83%E3%82%AF%E3%80%81%E6%8A%BD%E5%87%BA%E3%82%92%E8%A1%8C%E3%81%86/
  url_list = re.findall(pattern, dat)
  try:
    url = url_list[0]
  except IndexError:  #URLがなかった場合
    url = False
  return(url)

def convert_url(html_url):
  #末尾の"/"を削除
  if html_url[-1] == "/":
    html_url = html_url[:-1]
  #?以降を削除
  s = html_url.find("?")
  if s != -1:
    html_url = html_url[:s]
  #最新50 等のオプションを削除
  last_slush = html_url.rfind("/")  #最後の"/"を検索
  if "l" in html_url[last_slush:]:  #最後の"/"の後に"l"が存在するか
    html_url = html_url[:last_slush]  #最後の"/"以降を"/"含め削除
  #前100, 次100 等のオプションを削除
  if "-" in html_url[last_slush:]:  #最後の"/"の後に"-"が存在するか
    html_url = html_url[:last_slush]  #最後の"/"以降を"/"含め削除
  #"test/read.cgi/"を削除
  s = html_url.find("test/read.cgi/")
  html_url = html_url[:s] + html_url[s+14:]
  #途中の"dat/"と拡張子を追加
  last_slush = html_url.rfind("/")  #最後の"/"を検索
  html_url = html_url[:last_slush] + "/dat" + html_url[last_slush:] + ".dat"
  return(html_url)

def get_dat(url):
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36"}
  #戻り値の初期設定
  dat = ""
  dat_status = False
  #dat取得
  dat_res = requests.get(url, headers = headers)
  if dat_res.status_code == 200:
    dat_status = True
    dat = dat_res.content
    dat = dat.decode(encoding = "shift_jis", errors = "ignore")  #バイト列を文字列(Shift-JIS)に変換
  # print(type(dat))# test
  #test##############使い回しできそう########################
  # with open("test.txt", mode="wb") as file:
  #   file.write(dat)
  return(dat_status, dat)

def manual(i):
  url = str(input(f"Part{i}のurlを入力してください。"))
  return url

def output(filename, data):
  #ファイル作成・書き込み
  with open(output_dir + filename, mode="w", encoding="shift_jis") as file:
    file.write(data)
  #保存のメッセージ
  if filename[-1] == "t": #拡張子がdatか否か
    print(f"datを'{filename}'として保存しました。")
  else:
    print(f"htmlを'{filename}'として保存しました。")

def convert_data(dat):
  #"<>"毎に分割
  dat_elements = dat.split("<>")
  #初期化
  html_data = '''
<!DOCTYPE html>
<html lang="ja">
  <head>
  <meta charset="Shift_JIS">
  </head>
  <body text="#000000" link="#0000FF" alink="#FF0000" vlink="#660099" bgcolor="#EFEFEF">
  '''
  res = 1 #レス番
  n = int(len(dat_elements)/4)  #繰り返し回数
  #1レス目
  name = f'<font color="#228811"><b>{dat_elements[0]}</b></font>' #名前
  #(メール欄は無視)
  time_and_id = dat_elements[2] #日時とID
  body = dat_elements[3]  #本文
  #html_dataに書き加える
  html_data = f"{html_data}{res}：{name}：{time_and_id}<br>\n{body}<br><br>\n"
  #2レス目以降
  for i in range(n):
    #変数
    name = f'<font color="#228811"><b>{dat_elements[i*4]}</b></font>' #名前
    #(メール欄は無視)
    time_and_id = dat_elements[i*4+2] #日時とID
    body = dat_elements[i*4+3]  #本文
    #html_dataに書き加える
    html_data = f"{html_data}{res}：{name}：{time_and_id}<br>\n{body}<br><br>\n"
    res += 1
  html_data = html_data + "</body>\n</html>"
  # return(len(dat_elements))  #test
  return(html_data)


def main():
  parser = argparse.ArgumentParser(description="電子掲示板の複数partに別れたスレッドを結合します。")
  # 引数の設定
  parser.add_argument("latest_url", help = "最新のスレッドのURL")
  parser.add_argument("partnumber", type = int, help = "最新スレッドのpart数")
  parser.add_argument("-f", "--filename", default = default_filename(), help = "出力するファイル名")
  # parser.add_argument("--html", action="store_true", help = "datをhtmlに変換して保存 datも保存される")  #廃止
  parser.add_argument("-t", "--time", type = float, default = 1, help = "待機時間(秒)  デフォルト1")
  #引数の解析
  args = parser.parse_args()
  #変数
  url = args.latest_url
  partnumber = args.partnumber
  filename = args.filename
  # html = args.html  #廃止
  wait_time = args.time
  connected_dat = ""
  if wait_time < 0.5: #待機時間が短い場合は0.5秒にする。 
    wait_time = 0.5
    print("待機時間が短すぎます 0.5秒に変更しました。")
  #繰り返し開始
  for i in range(partnumber, 0, -1):
    #前スレurl検索
    if i != partnumber: #初回はスキップ
      url = find_url(dat)
      if not url:  #URLがなかった場合は手動入力
        url = manual(i)
    #htmlのurlをdatのurlに変換
    dat_url = convert_url(url)
      #datを取得
    while True:
      dat_status, dat = get_dat(dat_url)
      if dat_status:
        break
      else: #dat取得に失敗した場合
        url = manual(i)
        dat_url = convert_url(url)
    #datを結合
    connected_dat = dat + connected_dat
    #待機
    time.sleep(wait_time)
    print(f"Part{i}まで完了")
  #繰り返し終了
  #dat出力
  output(filename + ".dat", connected_dat)
  #html出力
  html_filename = filename + ".html"  #htmlのファイル名
  html_data = convert_data(connected_dat)
  output(html_filename, html_data)

if __name__ == "__main__":
  main()