def all_dictionaries_empty(dictionaries):
    for d in dictionaries:
        if d:
            return False
    return True

empty_dict_list = [{},{},{}]
not_empty_dict_list = [{1,2},{},{}]

print(all_dictionaries_empty(empty_dict_list))
print(all_dictionaries_empty(not_empty_dict_list))
