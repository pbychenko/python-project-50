import json
import yaml
import os


def format_data(data, format):
    if format == 'simple':
        return json.dumps(data, indent = 2).replace('"', '').replace(',', '')

    # if file_extension == '.yaml' or file_extension == '.yml':
    #     file1_data = yaml.load(open(file_path1, 'r'), Loader=yaml.FullLoader)
    #     file2_data = yaml.load(open(file_path2),Loader=yaml.FullLoader)
    
    # return [file1_data, file2_data]
    