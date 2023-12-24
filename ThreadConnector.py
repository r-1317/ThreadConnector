import argparse
import os

output_dir = "output/"

#関数の定義
def default_filename():
  assert os.path.isdir(output_dir)
  while True:
    n = 0
    fn = f"結合済みdat({n}).dat"
    if os.path.isfile(fn):
      n += 1
    else:
      return fn
      break


def main():
  parser = argparse.ArgumentParser(description="電子掲示板の複数partに別れたスレッドを結合します。")
  # 引数の設定
  parser.add_argument("latest_url", help = "最新のスレッドのURL")
  parser.add_argument("part_number", type = int, help = "最新スレッドのpart数")
  parser.add_argument("-f", "--filename", default = default_filename(), help = "出力するファイル名")

  args = parser.parse_args()


if __name__ == "__main__":
  main()