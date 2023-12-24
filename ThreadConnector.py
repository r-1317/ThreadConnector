import argparse

parser = argparse.ArgumentParser(description="電子掲示板の複数partに別れたスレッドを結合します。")

# 引数の設定
parser.add_argument("latest_url", help = "最新のスレッドのURL")
parser.add_argument("part_number", type = int, help = "最新スレッドのpart数")
parser.add_argument("")

args = parser.parse_args()
