import argparse

# ArgumentParser オブジェクトの作成
parser = argparse.ArgumentParser(description='Example program with positional arguments')

# 位置引数の追加
parser.add_argument('input', help='input file path')
parser.add_argument('output', help='output file path')

# 引数の解析
args = parser.parse_args()

# 引数の使用
print(f"Input file: {args.input}")
print(f"Output file: {args.output}")