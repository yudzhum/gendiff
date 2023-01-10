#!/usr/bin/env python3


from gendiff.gendiff import generate_diff
from gendiff.cli import get_arguments


def main():
    """Take two files and show diff"""

    args = get_arguments()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
