def dict_to_list(old_dict):
    new_list = []
    for item in old_dict.items():
        new_list.append(item[1])
    return new_list
