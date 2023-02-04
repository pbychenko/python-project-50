from .parser import parse_file
from .formatters import format


def generate_diff(file_path1, file_path2, type='stylish'):
    file1_data = parse_file(file_path1)
    file2_data = parse_file(file_path2)

    ast = get_ast(file1_data, file2_data)
    return format(ast, type)


def get_ast(data1, data2):
    set1 = set(data1.keys())
    set2 = set(data2.keys())

    all_keys = list(set1 | set2)
    all_keys.sort()

    def get_ast_element(key):
        if (key in data1 and isinstance(data1[key], dict)) and (key in data2 and isinstance(data2[key], dict)):
            return {'key': key, 'state': 'nested', 'children': get_ast(data1[key], data2[key])}

        if key in data1 and key in data2:
            if (data1[key] == data2[key]):
                return {'key': key, 'state': 'equal', 'value': data1[key]}
            return {'key': key, 'state': 'changed', 'value': data1[key], 'new_value': data2[key]}

        if key in data1:
            return {'key': key, 'state': 'removed', 'value': data1[key]}

        return {'key': key, 'state': 'added', 'value': data2[key]}

    return list(map(get_ast_element, all_keys))
