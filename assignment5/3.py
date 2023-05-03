def common_chars(str1, str2):
    common = set(str1) & set(str2) # find the common characters between the two strings
    if len(common) == 0:
        return "No common characters"
    else:
        return ''.join(sorted(common)) # sort the common characters in lexicographical order and return as a string

str1 = "hello"
str2 = "world"
result = common_chars(str1, str2)
print(result)
