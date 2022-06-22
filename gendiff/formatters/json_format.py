import json


def json_format(data):
    json_object = json.dumps(data, indent=4)
    return json_object
