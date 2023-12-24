import argparse
import os

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
  html_url = html_url.removeprefix("test/read.cgi/")

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
    dat_url = convert_url(url)


if __name__ == "__main__":
  main()