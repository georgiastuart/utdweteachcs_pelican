import json


def str_to_dict(value):
    return json.loads(''.join(value))