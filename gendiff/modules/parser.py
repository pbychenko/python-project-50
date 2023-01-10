import json
import yaml


def parse_files(file_path1, file_path2, format):
    if format == 'json':
        file1_data = json.load(open(file_path1, 'r'), object_hook=dict)
        file2_data = json.load(open(file_path2), object_hook=dict)

    if format == 'yaml':
        file1_data = yaml.load(open(file_path1, 'r'), Loader=yaml.FullLoader)
        file2_data = yaml.load(open(file_path2),Loader=yaml.FullLoader)
    
    return [file1_data, file2_data]
    