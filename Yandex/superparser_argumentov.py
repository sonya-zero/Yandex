import sys

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
args = parser.parse_args()

if args.arg:
    for i in args.arg:
        print(i)
else:
    print("no args")