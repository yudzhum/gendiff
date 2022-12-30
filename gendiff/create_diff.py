
def generate_diff(dict1, dict2):

    merged = dict1.keys() | dict2.keys()
    sorted_merged = sorted(merged)

    result = []
    for key in sorted_merged:
        if key not in dict1:
            value = f'+ {key}: {dict2[key]}'
        elif key not in dict2:  
            value = f'- {key}: {dict1[key]}'
        elif dict1[key] == dict2[key]:
            value = f'  {key}: {dict1[key]}'
        else:
            value = f'- {key}: {dict1[key]}\n+ {key}: {dict2[key]}'
    
        result.append(value)

    return '{\n' + '\n'.join(result) + '\n}'
