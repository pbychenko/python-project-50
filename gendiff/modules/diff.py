# import json
from .parser import parse_files
from .formatter import format_data
# import os

# def get_diff(data1, data2):
#     set1 = set(data1.keys())
#     set2 = set(data2.keys())
#     minus = set1 - set2
#     plus = set2 - set1
#     per = set1 & set2
#     d = {}
#     for el in minus:
#         d[f'- {el}'] = data1[el]

#     for el in plus:
#         d[f'+ {el}'] = data2[el]
    
#     for el in per:
#         if (data1[el] == data2[el]):
#             d[f'  {el}'] = data1[el]
#         else:
#             d[f'- {el}'] = data1[el]
#             d[f'+ {el}'] = data2[el]

#     # print(d)
#     def f(e):
#         # if e[0] == '-' or e[0] == '+':
#         #     return e[2:]
#         return e[2:]
    
    
#     sortedKeys = list(d.keys())
#     sortedKeys.sort(key=f)
#     # print(sortedKeys)
#     result = {}
#     for el in sortedKeys:
#         result[el] = d[el]
#     return format_data(result, 'simple')


# def generate_diff(file_path1, file_path2):
#     [file1_data, file2_data] = parse_files(file_path1, file_path2)
#     return get_diff(file1_data, file2_data)

def generate_diff(file_path1, file_path2):
    [file1_data, file2_data] = parse_files(file_path1, file_path2)
    ast = get_ast(file1_data, file2_data)
    print('ast', ast)
    return ast

def get_ast(data1, data2):
    
    set1 = set(data1.keys())
    set2 = set(data2.keys())
    # minus = set1 - set2
    # plus = set2 - set1
    # per = set1 & set2

    all_keys = set1 | set2
    # print(all_keys)
    
    def get_ast_element(key):
        if (data1.get(key) and data1[key] is dict) and (data2.get(key) and data2[key] is dict):
            print('key', key)
            return { 'key': key, 'state': 'nested', 'children': get_ast(data1[key], data2[key]) }
        if data1.get(key) and data2.get(key):
            if (data1[key] == data2[key]):
                return { 'key':key, 'state': 'equal', 'value': data1[key] }
            return { 'key': key, 'state': 'changed', 'value': data1[key], 'new_value': data2[key] }
        if data1.get(key):
            return { 'key': key, 'state': 'removed', 'value': data1[key] }
        return { 'key': key, 'state': 'added', 'value': data2[key] }



    # print('minus', minus)
    # print('plus', plus)
    # print('per', per)
    # d = {}
    # # if (set1 != set()) {
        
    # # }

    return list(map(get_ast_element, all_keys))

    