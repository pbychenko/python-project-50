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

def formatElement(el, indent_count):
    indents = ' '*indent_count
    if isinstance(el, dict):
        return '{\n' + f'{indents}{el}' + f"\n{indents}" + '}'
    return el
    
def stylish(data):
    indent_count = 2
    indents = ' '*indent_count
    
    def getElement(el):
        if (el['state'] == 'nested'):
            return f"{indents}  {el['key']}: {formatElement(stylish(el['children']), indent_count + 2)}"
        if (el['state'] == 'added'):
            return f"{indents}+ {el['key']}: {formatElement(el['value'], indent_count + 2)}"
        if (el['state'] == 'removed'):
            return f"{indents}- {el['key']}: {formatElement(el['value'], indent_count + 2)}"
        if (el['state'] == 'equal'):
            return f"{indents}  {el['key']}: {formatElement(el['value'], indent_count + 2)}"
        if (el['state'] == 'changed'):
            return f"{indents}- {el['key']}: {formatElement(el['value'], indent_count + 2)}'\n'{indents}+ {el['key']}: {formatElement(el['new_value'], indent_count + 2)}"
    
    # print(list(map(getElement, data)))
    result = '{\n' + f"{indents}" +'\n'.join(list(map(getElement, data))) + '\n}'    
    # result = f"{' '*indent_count}" +'\n'.join(list(map(getElement, data)))

    # result = json.dumps(data, indent = 2).replace('"', '').replace(',', '')
    # print(result)
    return result
    