def get_max_min(dict):
    values = dict.values()
    return (max(values), min(values))

dict = {'a': 1, 'b': 2, 'c': 3}
print(get_max_min(dict))
