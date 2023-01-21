def formatElement(el, indent_count):
    indents = ' '*indent_count
    if not isinstance(el, dict):
        return el
    result = []

    for k, v in el.items():
        result.append(f'  {indents}{k}: {formatElement(v, indent_count + 4)}')
    result_str = '\n'.join(result)

    return '{\n' + f'{result_str}' + f"\n{' '*(indent_count - 2)}" + '}'
    
def stylish(data, indent_count = 2 ):
    indents = ' '*indent_count
    
    def getElement(el):
        if (el['state'] == 'nested'):
            return f"{indents}  {el['key']}: {stylish(el['children'], indent_count + 4)}"
        
        if (el['state'] == 'added'):
            return f"{indents}+ {el['key']}: {formatElement(el['value'], indent_count + 4)}"
        if (el['state'] == 'removed'):
            return f"{indents}- {el['key']}: {formatElement(el['value'], indent_count + 4)}"
        if (el['state'] == 'equal'):
            return f"{indents}  {el['key']}: {formatElement(el['value'], indent_count + 4)}"
        if (el['state'] == 'changed'):
            return f"{indents}- {el['key']}: {formatElement(el['value'], indent_count + 4)}\n{indents}+ {el['key']}: {formatElement(el['new_value'], indent_count + 4)}"
    
    result = ('{\n' + '\n'.join(list(map(getElement, data))) + f"\n{' '*(indent_count - 2)}" + '}').replace('None', 'null').replace('True', 'true').replace('False', 'false')
    return result
    