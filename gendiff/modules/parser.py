import json
import yaml
import os


def parse_files(file_path1, file_path2):
    _, file_extension = os.path.splitext(file_path1)
    # print(file_extension)
    if file_extension == '.json':
        file1_data = json.load(open(file_path1, 'r'), object_hook=dict)
        file2_data = json.load(open(file_path2), object_hook=dict)

    if file_extension == '.yaml' or file_extension == '.yml':
        file1_data = yaml.load(open(file_path1, 'r'), Loader=yaml.FullLoader)
        file2_data = yaml.load(open(file_path2),Loader=yaml.FullLoader)
    
    return [file1_data, file2_data]
    