import string

def is_pangram(string):
    """Checks if the given string is a pangram."""
    # Create a set of all alphabets
    alphabets = set([chr(x) for x in range(97,97+26)])
    # Convert the string to lower case and remove all non-alphabetic characters
    string = set(filter(str.isalpha, string.lower()))
    # Check if the set of alphabets is a subset of the set of characters in the string
    return alphabets.issubset(string)


string = "The quick brown fox jumps over the lazy dog"
if is_pangram(string):
    print(f"{string} is a pangram")
else:
    print(f"{string} is not a pangram")
