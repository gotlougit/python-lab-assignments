fname = input("Enter filename: ")
with open(fname) as f:
    txt = f.read().split()
    count = 0
    for word in txt:
        count += len(word.split(","))
    print(f"Number of words in text is/are: {count}")
