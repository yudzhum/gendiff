import argparse
import json

import yaml 
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def open_file(filepath):
    """Check format, open file, return dictionary"""
    
    if filepath.endswith('.json'):
        data = json.load(open(filepath))
        return data
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        data = yaml.load(open(filepath), Loader=Loader)
        return data


def parse():
    """Parse argument and return two dictionaries"""

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    dict1 = open_file(args.first_file)
    dict2 = open_file(args.second_file)
    return dict1, dict2
