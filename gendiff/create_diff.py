import argparse
import json


def parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('-f', '--format', help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args

args = parser()

def generate_diff(args):
    dict1 = json.load(open(args.first_file))
    dict2 = json.load(open(args.second_file))

    keys1 = sorted(dict1.keys())
    keys2 = sorted(dict2.keys())

    result = []
    for i in range(len(keys1)):
        key = keys1[0]
        if key == keys2[0]:
            if dict1[key] == dict2[key]:
                result.append(f'  {key}: {dict1[key]}')
                keys1.pop(0)
                keys2.pop(0)
            else:
                result.append(f'- {key}:{dict1[key]}')
                result.append(f'+ {key}:{dict2[key]}')
                keys1.pop(0)
                keys2.pop(0)
        elif key in keys2:
            result.append(f'+ {keys2[0]}: {dict2[keys2[0]]}')
            keys2.pop(0)
        else:
            result.append(f'- {key}: {dict1[key]}')
            keys1.pop(0)

    for key in keys2:
        result.append(f'+ {key}: {dict2[key]}')
        keys2.pop(0)

    print('{\n' + '\n'.join(result) + '\n}')
    return '{\n' + '\n'.join(result) + '\n}'


def main():
    generate_diff(args)


if __name__ == '__main__':
    main()
