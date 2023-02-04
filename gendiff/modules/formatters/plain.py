def formatElement(el):
    if isinstance(el, dict):
        return '[complex value]'

    if isinstance(el, bool):
        return str(el).lower()

    if el is None:
        return 'null'

    if isinstance(el, str):
        return f"'{el}'"

    return el


def get_path(path, key):
    return key if path == '' else f'{path}.{key}'


def plain(data, path=''):
    def getElement(el):
        full_path = get_path(path, el['key'])
        value = formatElement(el['value']) if 'value' in el else None

        if (el['state'] == 'nested'):
            return plain(el['children'], full_path)

        if (el['state'] == 'added'):
            return f"Property '{full_path}' was added with value: {value}"

        if (el['state'] == 'removed'):
            return f"Property '{full_path}' was removed"

        if (el['state'] == 'equal'):
            return ''

        if (el['state'] == 'changed'):
            return f"Property '{full_path}' was updated. From {value} to {formatElement(el['new_value'])}"

    filtered = filter(lambda el: el != '', map(getElement, data))
    result = '\n'.join(list(filtered))

    return result
