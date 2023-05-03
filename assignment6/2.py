fname = input("Enter filename: ")
print(f"\nHere are the contents of file {fname}:\n")
with open(fname) as f:
    while True:
        nextline = f.readline()
        if not nextline:
            break
        print(nextline[:-1])
