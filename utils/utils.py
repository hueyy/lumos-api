import json
import jsonpickle


def dict_to_list(old_dict):
    new_list = []
    for item in old_dict.items():
        new_list.append(item[1])
    return new_list


def object_to_dict(obj):
    return json.loads(jsonpickle.encode(obj, unpicklable=False))
