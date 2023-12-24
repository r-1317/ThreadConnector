import argparse
import os
import requests

output_dir = "output/"

#関数の定義
def default_filename():
  assert os.path.isdir(output_dir)
  n = 0
  while True:
    fn = f"結合済みdat({n}).dat"
    # print(output_dir + fn) #デバッグ
    if os.path.isfile(output_dir + fn):
      n += 1
    else:
      return fn
      break

def convert_url(html_url):
  #末尾の"/"を削除
  if html_url[-1] == "/":
    html_url = html_url[:-1]
  s = html_url.find("test/read.cgi/")
  html_url = html_url[:s] + html_url[s+14:]
  last_slush = html_url.rfind("/")
  html_url = html_url[:last_slush] + "/dat" + html_url[last_slush:] + ".dat"
  return(html_url)

def get_dat(url):
  dat = ""
  dat_status = False
  dat_res = requests.get(url)
  if dat_res.status_code == 200:
    dat_status = True
    dat = dat_res.content
  print(type(dat))# test
  return(dat_status)



def main():
  parser = argparse.ArgumentParser(description="電子掲示板の複数partに別れたスレッドを結合します。")
  # 引数の設定
  parser.add_argument("latest_url", help = "最新のスレッドのURL")
  parser.add_argument("partnumber", type = int, help = "最新スレッドのpart数")
  parser.add_argument("-f", "--filename", default = default_filename(), help = "出力するファイル名")
  #引数の解析
  args = parser.parse_args()
  #
  url = args.latest_url
  partnumber = args.partnumber
  filename = args.filename
  #繰り返し開始
  for i in range(partnumber, 0, -1):
    #htmlのurlをdatのurlに変換
    dat_url = convert_url(url)
    #datを取得
    dat = get_dat(dat_url)


if __name__ == "__main__":
  main()