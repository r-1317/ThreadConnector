import argparse
import os
import requests
import time
import re

output_dir = "output/"

#関数の定義
def default_filename():
  assert os.path.isdir(output_dir)
  n = 0
  while True:
    fn = f"結合済み({n}).dat"
    # print(output_dir + fn) #デバッグ
    if os.path.isfile(output_dir + fn):
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
    dat = dat.decode(encoding = "shift_jis", errors = "replace")  #バイト列を文字列(Shift-JIS)に変換
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
  with open(output_dir + filename, mode="w") as file:
    file.write(data)
  #保存のメッセージ
  if filename[-1] == "t": #datか否か
    print(f"datを'{filename}'として保存しました。")
  else:
    print(f"htmlを'{filename}'として保存しました。")

def convert_data(dat):
  #######未実装#######
  return("未実装")


def main():
  parser = argparse.ArgumentParser(description="電子掲示板の複数partに別れたスレッドを結合します。")
  # 引数の設定
  parser.add_argument("latest_url", help = "最新のスレッドのURL")
  parser.add_argument("partnumber", type = int, help = "最新スレッドのpart数")
  parser.add_argument("-f", "--filename", default = default_filename(), help = "出力するファイル名")
  parser.add_argument("--html", action="store_false", help = "datをhtmlに変換して保存 datも保存される")
  parser.add_argument("-t", "time", type = float, default = 1 help = "待機時間(秒)  デフォルト1")
  #引数の解析
  args = parser.parse_args()
  #変数
  url = args.latest_url
  partnumber = args.partnumber
  filename = args.filename
  html = args.html
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
  output(filename, connected_dat)
  #html出力
  if html:
    html_filename = filename[:-3] + "html"  #htmlのファイル名
    html_data = convert_data(connected_dat)
    output(filename, html_data)

if __name__ == "__main__":
  main()