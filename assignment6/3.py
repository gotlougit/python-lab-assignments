fname1 = input("Enter first filename: ")
fname2 = input("Enter second filename: ")

print("\nHere are the contents of combined file:\n")

with open(fname1) as f1:
    with open(fname2) as f2:
        while True:
            nl1 = f1.readline()
            nl2 = f2.readline()
            if (not nl1) and (not nl2):
                break
            nl1 = nl1[:-1] + " " + nl2[:-1]
            print(nl1)
