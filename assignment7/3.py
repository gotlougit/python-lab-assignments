def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
result = common_member(list1, list2)
print(result) # False

list3 = [1, 2, 3, 4]
list4 = [4, 5, 6, 7]
result = common_member(list3, list4)
print(result) # True
