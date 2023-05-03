def separate_strings(string):
    once = "" # empty string to store characters that occur only once
    multiple = "" # empty string to store characters that occur more than once
    for char in string:
        if string.count(char) == 1: # check if character occurs only once
            once += char
        elif string.count(char) > 1: # check if character occurs more than once
            multiple += char
    return once, multiple

string = "Hello, world!"
once_chars, multiple_chars = separate_strings(string)
print("Characters that occur only once:", once_chars)
print("Characters that occur more than once:", multiple_chars)
