def count_values(lst, key, value):
    count = 0
    for d in lst:
        if d[key] == value:
            count += 1
    return count

lst = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
key = 'success'
value = True
print(count_values(lst, key, value))
