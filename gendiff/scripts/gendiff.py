#!/usr/bin/env python3


import argparse
from gendiff.parse import parse_data
from gendiff.create_diff import generate_diff
from gendiff.formatters.stylish import stylish


def main():
    """Take two files and show diff"""

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    dict1 = parse_data(args.first_file)
    dict2 = parse_data(args.second_file)

    diff = generate_diff(dict1, dict2)
    if args.format == 'stylish':
        print(stylish(diff))


if __name__ == '__main__':
    main()
