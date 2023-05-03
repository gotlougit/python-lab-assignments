def first_repeated_word(string):
    words = string.split() # split the string into words
    seen_words = set() # set to keep track of seen words
    for word in words:
        if word in seen_words: # check if word has been seen before
            return word # return the repeated word
        seen_words.add(word) # add word to seen_words set if it hasn't been seen before
    return "No repeated words found." # return this if there are no repeated words

string = "the quick brown fox jumps over the lazy dog the dog jumps over the fence"
result = first_repeated_word(string)
print(result)
