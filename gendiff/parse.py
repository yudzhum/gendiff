import argparse
import json


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    dict1 = json.load(open(args.first_file))
    dict2 = json.load(open(args.second_file))
    return dict1, dict2
