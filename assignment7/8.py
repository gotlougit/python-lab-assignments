def smallest_second_index(tuples):
    # Initialize the smallest tuple and its second index value
    smallest_tuple = tuples[0]
    smallest_second_index = smallest_tuple[1]

    # Iterate over the tuples to find the smallest second index value
    for t in tuples[1:]:
        if t[1] < smallest_second_index:
            smallest_tuple = t
            smallest_second_index = t[1]

    return smallest_tuple

tuples = [(1, 5), (2, 3), (3, 8), (4, 2), (5, 4)]
smallest = smallest_second_index(tuples)
print(smallest)
