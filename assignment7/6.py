def to_sorted_unique_array(a, b):
    # Create a set of the input values
    values = {a, b}

    # Convert the set to a list and sort it
    sorted_list = sorted(list(values))

    return sorted_list

a = 5
b = 2.5
sorted_unique_array = to_sorted_unique_array(a, b)
print(sorted_unique_array)
