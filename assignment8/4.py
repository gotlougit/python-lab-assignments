def check_key(dict, key):
    if key in dict.keys():
        return True
    else:
        return False

dict = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
print(check_key(dict, key))
