fname = input("Enter filename: ")
k = int(input("Enter row size: "))
i = 0
j = 0
with open(fname, "w") as f:
    while i < 26:
        while j < k and i < 26:
            f.write(chr(65 + i) + " ")
            i += 1
            j += 1
        j = 0
        f.write("\n")
