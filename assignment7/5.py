def is_circularly_identical(list1, list2):
    if len(list1) != len(list2):
        return False

    # Concatenate list1 with itself
    concatenated = list1 + list1

    # Check if list2 is a sublist of the concatenated list
    for i in range(len(concatenated) - len(list2) + 1):
        if concatenated[i:i+len(list2)] == list2:
            return True

    return False

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 1, 2, 3]

if is_circularly_identical(list1, list2):
    print("The lists are circularly identical.")
else:
    print("The lists are not circularly identical.")
