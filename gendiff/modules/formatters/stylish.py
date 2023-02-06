indents = '  '
depth_step = '    '
indent_template = '  '


def formatElement(el, depth):
    if isinstance(el, bool):
        return str(el).lower()

    if el is None:
        return 'null'

    if not isinstance(el, dict):
        return el

    result = []
    step_distant = depth_step * depth
    closing_indents = depth_step * (depth - 1)

    for k, v in el.items():
        result.append(f'{step_distant}{k}: {formatElement(v, depth + 1)}')

    result_str = '\n'.join(result)

    return '{\n' + f'{result_str}' + f"\n{closing_indents}" + '}'


def stylish(data, depth=1):
    step_distant = depth_step * (depth - 1)

    def get_element(el):
        if (el['state'] == 'nested'):
            return f"{step_distant}{indents}  {el['key']}: {stylish(el['children'], depth + 1)}"

        value = formatElement(el['value'], depth + 1)

        if (el['state'] == 'added'):
            return f"{step_distant}{indents}+ {el['key']}: {value}"

        if (el['state'] == 'removed'):
            return f"{step_distant}{indents}- {el['key']}: {value}"

        if (el['state'] == 'equal'):
            return f"{step_distant}{indents}  {el['key']}: {value}"

        if (el['state'] == 'changed'):
            return f"{step_distant}{indents}- {el['key']}: {value}\n{step_distant}{indents}+ {el['key']}: {formatElement(el['new_value'], depth + 1)}"

    result = '{\n' + '\n'.join(list(map(get_element, data))) + f"\n{step_distant}" + '}'

    return result
