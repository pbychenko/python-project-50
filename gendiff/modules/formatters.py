import json
import yaml
import os


# def format_data(data, format):
#     if format == 'stylish':
#         return json.dumps(data, indent = 2).replace('"', '').replace(',', '')

    # if file_extension == '.yaml' or file_extension == '.yml':
    #     file1_data = yaml.load(open(file_path1, 'r'), Loader=yaml.FullLoader)
    #     file2_data = yaml.load(open(file_path2),Loader=yaml.FullLoader)
    
    # return [file1_data, file2_data]
def stylish(data):
    # print(data)
    
    def getElement(el):
        if (el['state'] == 'nested'):
            return f" {el['key']}: {stylish(el['children'])}"
        if (el['state'] == 'added'):
            return f"+ {el['key']}: {el['value']}\n"
        if (el['state'] == 'removed'):
            return f"- {el['key']}: {el['value']}\n"
        if (el['state'] == 'equal'):
            return f"  {el['key']}: {el['value']}\n"
        if (el['state'] == 'changed'):
            return f"- {el['key']}: {el['value']}\n+ {el['key']}: {el['new_value']}\n"
    
    result = ''.join(list(map(getElement, data)))   

    # result = json.dumps(data, indent = 2).replace('"', '').replace(',', '')
    # print(result)
    return result
    