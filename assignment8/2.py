def unzip_list(lst):
    return list(zip(*lst))

lst = [(1, 2), (3, 4), (5, 6)]
print(unzip_list(lst))
