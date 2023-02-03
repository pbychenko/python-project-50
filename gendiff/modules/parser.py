import json
import yaml
import os


def parse_file(file_path):
    _, file_extension = os.path.splitext(file_path)

    extensions_map = {
        '.json': lambda path: json.load(open(path, 'r'), object_hook=dict),
        '.yaml': lambda path: yaml.load(open(path, 'r'), Loader=yaml.FullLoader),
        '.yml': lambda path: yaml.load(open(path, 'r'), Loader=yaml.FullLoader)
    }

    return extensions_map[file_extension](file_path)
