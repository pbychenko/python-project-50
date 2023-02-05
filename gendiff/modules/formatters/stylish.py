# def formatElement(el, indent_count):
#     if isinstance(el, bool):
#         return str(el).lower()

#     if el is None:
#         return 'null'

#     if not isinstance(el, dict):
#         return el

#     result = []
#     indents = ' ' * indent_count

#     for k, v in el.items():
#         result.append(f'  {indents}{k}: {formatElement(v, indent_count + 4)}')
#     result_str = '\n'.join(result)

#     return '{\n' + f'{result_str}' + f"\n{' '*(indent_count - 2)}" + '}'


# def stylish(data, indent_count=2):
#     indents = ' ' * indent_count    

#     def get_element(el):
#         if (el['state'] == 'nested'):
#             return f"{indents}  {el['key']}: {stylish(el['children'], indent_count + 4)}"
        
#         value = formatElement(el['value'], indent_count + 4)

#         if (el['state'] == 'added'):
#             return f"{indents}+ {el['key']}: {value}"

#         if (el['state'] == 'removed'):
#             return f"{indents}- {el['key']}: {value}"

#         if (el['state'] == 'equal'):
#             return f"{indents}  {el['key']}: {value}"

#         if (el['state'] == 'changed'):
#             return f"{indents}- {el['key']}: {value}\n{indents}+ {el['key']}: {formatElement(el['new_value'], indent_count + 4)}"        


    
#     result = '{\n' + '\n'.join(list(map(get_element, data))) + f"\n{' '*(indent_count - 2)}" + '}'

#     return result

indent_step = 4
indent_template = '  '


def formatElement(el, depth):
    if isinstance(el, bool):
        return str(el).lower()

    if el is None:
        return 'null'

    if not isinstance(el, dict):
        return el

    result = []
    indents = indent_template * (depth + indent_step + 1)
    closing_indents = indent_template * (depth + 1)

    for k, v in el.items():
        result.append(f'{indents}{k}: {formatElement(v, depth + indent_step)}')
    result_str = '\n'.join(result)
    # print(' result_str', result_str)

    return '{\n' + f'{result_str}' + f"\n{closing_indents}" + '}'


def stylish(data, depth=1):
    indents = indent_template * depth


    def get_element(el):
        if (el['state'] == 'nested'):
            return f"{indents}  {el['key']}: {stylish(el['children'], depth + indent_step)}"
        
        value = formatElement(el['value'], depth)

        if (el['state'] == 'added'):
            return f"{indents}+ {el['key']}: {value}"

        if (el['state'] == 'removed'):
            return f"{indents}- {el['key']}: {value}"

        if (el['state'] == 'equal'):
            return f"{indents}  {el['key']}: {value}"

        if (el['state'] == 'changed'):
            return f"{indents}- {el['key']}: {value}\n{indents}+ {el['key']}: {formatElement(el['new_value'], depth)}"    


    
    result = '{\n' + '\n'.join(list(map(get_element, data))) + f"\n{indent_template * (depth - 1)}" + '}'

    return result
