def to_list_of_dicts(names, codes):
    list_of_dicts = []

    for i in range(len(names)):
        dict_item = {'color_name': names[i], 'color_code': codes[i]}
        list_of_dicts.append(dict_item)

    return list_of_dicts

names = ["Black", "Red", "Maroon", "Yellow"]
codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]

list_of_dicts = to_list_of_dicts(names, codes)
print(list_of_dicts)
