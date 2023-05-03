def find_substring(string, substring):
    index = string.find(substring) # use the find() method to find the index of the substring in the string
    if index == -1: # if substring is not found, return 'Not found'
        return 'Not found'
    else:
        return index

string = "Hello, world!"
substring = "world"
result = find_substring(string, substring)
print(result)
