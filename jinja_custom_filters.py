import json


def get_headers(value):
    for index, pair in enumerate(value):
        value[index] = (x.strip() for x in pair.split(':'))
    return value


def load_toc(value):
    print(value)
    with open(value, 'r') as fp:
        return json.load(fp)

def test():
    print("it works!")

