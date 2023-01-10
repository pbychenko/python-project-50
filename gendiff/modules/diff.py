import json
from .parser import parse_files
import os

def get_diff(data1, data2):
    # print(data1)
    # print(data2)
    set1 = set(data1.keys())
    set2 = set(data2.keys())
    # print(set1)
    # print(set2)
    minus = set1 - set2
    plus = set2 - set1
    per = set1 & set2
    # print(minus)
    # print(plus)
    # print(per)
    d = {}
    # print(type(d))
    for el in minus:
        d[f'- {el}'] = data1[el]

    for el in plus:
        d[f'+ {el}'] = data2[el]
    
    for el in per:
        if (data1[el] == data2[el]):
            d[el] = data1[el]
        else:
            d[f'- {el}'] = data1[el]
            d[f'+ {el}'] = data2[el]
    # print(d.values())

    # print(d)
    def f(e):
        if e[0] == '-' or e[0] == '+':
            return e[2:]
        return e
    
    
    sortedKeys = list(d.keys())
    sortedKeys.sort(key=f)
    # print(sortedKeys)
    result = {}
    for el in sortedKeys:
        result[el] = d[el]
    # print(json.dumps(result))
    return json.dumps(result)

    # list(d.keys()).sort(key=f)
    

    # print(d)



def generate_diff(file_path1, file_path2, format):
    [file1_data, file2_data] = parse_files(file_path1, file_path2, format)
    return get_diff(file1_data, file2_data)
    