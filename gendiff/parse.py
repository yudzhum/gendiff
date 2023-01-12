import json
import yaml


def parse_data(source_data, format):
    """
    Take data in formats json or yaml.
    Return dictionary.
    """

    if format == "json":
        return json.loads(source_data)
    elif format == 'yaml' or format == 'yml':
        return yaml.safe_load(source_data)
