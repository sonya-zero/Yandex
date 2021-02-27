import argparse

parser = argparse.ArgumentParser()
parser.add_argument("barbie")
parser.add_argument("cars")
parser.add_argument("movie")
args = parser.parse_args()

print(args.barbie)
print(args.cars)
print(args.movie)