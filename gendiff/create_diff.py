
def generate_diff(dict1, dict2):

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
                result.append(f'- {key}: {dict1[key]}')
                result.append(f'+ {key}: {dict2[key]}')
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

    return '{\n' + '\n'.join(result) + '\n}'
