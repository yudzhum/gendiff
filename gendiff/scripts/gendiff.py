#!/usr/bin/env python3


import argparse
from gendiff.create_diff import generate_diff
from gendiff.formatters.stylish import stylish


def main():
    """Take two files and show diff"""

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', choices=['stylish'],
                        default='stylish', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    if args.format == 'stylish':
        diff = generate_diff(args.first_file, args.second_file, stylish)
        print(diff)


if __name__ == '__main__':
    main()
