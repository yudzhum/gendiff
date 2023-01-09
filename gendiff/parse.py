import json

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def parse_data(filepath):
    """Check format, open file, return dictionary"""

    if filepath.endswith('.json'):
        data = json.load(open(filepath))
        return data
    elif filepath.endswith('.yaml') or filepath.endswith('.yml'):
        data = yaml.load(open(filepath), Loader=Loader)
        return data
