def remove_empty_tuples(lst):
    return [t for t in lst if t]

lst = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(remove_empty_tuples(lst))
