import json
import os


def get_diff(data1, data2):
    print(data1)
    print(data2)
    set1 = set(data1.keys())
    set2 = set(data2.keys())
    print(set1)
    print(set2)
    minus = set1 - set2
    plus = set2 - set1
    per = set1 & set2
    print(minus)
    print(plus)
    print(per)
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
    print(sortedKeys)

    # list(d.keys()).sort(key=f)
    

    # print(d)



def generate_diff(file_path1, file_path2):
    # print('here')
    # print(os.getcwd())
    # print(file_path1)
    fulldir1 = os.path.join(os.getcwd(), 'gendiff', 're', file_path1)
    fulldir2 = os.path.join(os.getcwd(), 'gendiff', 're', file_path2)
    file1_data = json.load(open(fulldir1, 'r'), object_hook=dict)
    file2_data = json.load(open(fulldir2), object_hook=dict)
    return get_diff(file1_data, file2_data)
    