from .stylish import stylish
from .plain import plain
from .json import format_to_json


def format(type):
    formats_map = {
        'stylish': stylish,
        'plain': plain,
        'json': format_to_json
    }

    return formats_map[type]
