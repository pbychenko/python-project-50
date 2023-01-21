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
    if not isinstance(el, dict):
        return el
    
    # print('el', el)
    result = []

    for k, v in el.items():
        result.append(f'{indents}{k}: {v}')
    result_str = '\n'.join(result)
    print(indent_count)
    print('result_str', result_str)


    return '{\n' + f'{result_str}' + f"\n{' '*(indent_count - 4)}" + '}'
    
def stylish(data, indent_count = 2 ):
    indents = ' '*indent_count
    
    def getElement(el):
        if (el['state'] == 'nested'):
            # return f"{indents}  {el['key']}: {formatElement(stylish(el['children']), indent_count + 2)}"
            return f"{indents}  {el['key']}: {stylish(el['children'], indent_count + 4)}"
        
        if (el['state'] == 'added'):
            return f"{indents}+ {el['key']}: {formatElement(el['value'], indent_count + 4)}"
        if (el['state'] == 'removed'):
            return f"{indents}- {el['key']}: {formatElement(el['value'], indent_count + 4)}"
        if (el['state'] == 'equal'):
            return f"{indents}  {el['key']}: {formatElement(el['value'], indent_count + 4)}"
        if (el['state'] == 'changed'):
            return f"{indents}- {el['key']}: {formatElement(el['value'], indent_count + 4)}\n{indents}+ {el['key']}: {formatElement(el['new_value'], indent_count + 4)}"
    
    # print(list(map(getElement, data)))
    # result = '{\n' + f"{indents}" +'\n'.join(list(map(getElement, data))) + '\n}'
    # t1 = list(map(getElement, data))
    # print(t1)
    # flatten = [item for sublist in t1 for item in sublist]
    result = '{\n' + '\n'.join(list(map(getElement, data))) + f"\n{' '*(indent_count - 2)}" + '}'
    # result = '{\n' + '\n'.join(flatten) + f"\n{' '*(indent_count - 2)}" + '}'
    return result
    