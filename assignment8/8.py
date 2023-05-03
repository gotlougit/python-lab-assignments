from collections import defaultdict

def create_dict(lst1, lst2):
    d = defaultdict(set)
    for k, v in zip(lst1, lst2):
        d[k].add(v)
    return d

lst1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
lst2 = [1, 2, 2, 3]
print(create_dict(lst1, lst2))
