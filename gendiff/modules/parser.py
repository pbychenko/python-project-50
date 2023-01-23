import json
import yaml
import os


def parse_file(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension == '.json':
        file_data = json.load(open(file_path, 'r'), object_hook=dict)

    if file_extension == '.yaml' or file_extension == '.yml':
        print('here')
        f = open(file_path, 'r')
        print('print(f.read())', f.read())
        file_data = yaml.load(open(file_path, 'r'), Loader=yaml.FullLoader)
    return file_data
    