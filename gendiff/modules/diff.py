from .parser import parse_file
from .formatters.stylish import stylish
from .formatters.plain import plain
from .formatters.json import format_to_json

def generate_diff(file_path1, file_path2, type = 'stylish'):
    file1_data = parse_file(file_path1)
    file2_data = parse_file(file_path2)

    print('file_path1', file_path1)
    print('file_path2', file_path2)
    print('file1_data', file1_data)
    print('file2_data', file2_data)
    print('type', type)
    
    ast = get_ast(file1_data, file2_data)
    # print('tt',f'{isinstance(ast, list)}')
    # l = [1,2,3]
    # print(type(l))
    if type == 'stylish' or type == None:
        return stylish(ast)

    if type == 'plain':
        return plain(ast)
    
    if type == 'json':
        return format_to_json(ast)

def get_ast(data1, data2):    
    set1 = set(data1.keys())
    set2 = set(data2.keys())

    all_keys = list(set1 | set2)
    all_keys.sort()
    
    def get_ast_element(key):
        if (key in data1 and isinstance(data1[key], dict)) and (key in data2 and isinstance(data2[key], dict)):
            return { 'key': key, 'state': 'nested', 'children': get_ast(data1[key], data2[key]) }
        if key in data1 and key in data2:
            if (data1[key] == data2[key]):
                return { 'key':key, 'state': 'equal', 'value': data1[key] }
            return { 'key': key, 'state': 'changed', 'value': data1[key], 'new_value': data2[key] }
        if key in data1:
            return { 'key': key, 'state': 'removed', 'value': data1[key] }
        return { 'key': key, 'state': 'added', 'value': data2[key] }

    return list(map(get_ast_element, all_keys))

    