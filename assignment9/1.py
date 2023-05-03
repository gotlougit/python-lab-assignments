def count_upper_lower(string):
    """Counts the number of upper and lower case letters in a given string."""
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count


string = "Hello World!"
upper_count, lower_count = count_upper_lower(string)
print(f"Number of upper case letters: {upper_count}")
print(f"Number of lower case letters: {lower_count}")
