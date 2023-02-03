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


def plain(data, prev_keys=[]):
    def getElement(el):
        new_keys = prev_keys[:]
        new_keys.append(el['key'])

        if (el['state'] == 'nested'):
            return plain(el['children'], new_keys)

        if (el['state'] == 'added'):
            return f"Property '{'.'.join(new_keys)}' was added with value: {formatElement(el['value'])}"

        if (el['state'] == 'removed'):
            return f"Property '{'.'.join(new_keys)}' was removed"

        if (el['state'] == 'equal'):
            return ''

        if (el['state'] == 'changed'):
            return f"Property '{'.'.join(new_keys)}' was updated. From {formatElement(el['value'])} to {formatElement(el['new_value'])}"

    filtered = filter(lambda el: el != '', map(getElement, data))
    result = '\n'.join(list(filtered))

    return result
