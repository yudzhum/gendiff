#!/usr/bin/env python3


from gendiff.parse import parse
from gendiff.create_diff import generate_diff
from gendiff.formatters.stylish import stylish


def main():
    dict1, dict2 = parse()
    diff = generate_diff(dict1, dict2)
    print(stylish(diff))


if __name__ == '__main__':
    main()
