import argparse


def get_arguments():
    """Parse arguments"""

    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', choices=['stylish', 'plain', 'json'],
                        default='stylish', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args
