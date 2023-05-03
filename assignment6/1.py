fname = input("Enter filename: ")
print(f"\nHere are the contents of file {fname}:\n")
with open(fname) as f:
    print(f.read())
