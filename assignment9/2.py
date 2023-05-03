def is_palindrome(string):
    """Checks if the given string is a palindrome."""
    # Remove all whitespace and convert to lower case
    string = string.replace(" ", "").lower()
    # Check if string is equal to its reverse
    return string == string[::-1]

string = "A man a plan a canal Panama"
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
