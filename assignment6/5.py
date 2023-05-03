for i in range(0, 26):
    fname = chr(65 + i) + ".txt"
    with open(fname, "w") as f:
        f.write("this is a text file\n")
