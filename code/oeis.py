def more(sequence):
    i = 0
    s = ""
    c = 0
    while c < 260:
        x = sequence(i)
        entry = str(x) + ","
        l = len(entry)
        s = s + entry
        c = c + l
        i = i + 1
    return s


def bfile(sequence, m=30):
    name = sequence.__name__.replace("A", "b")
    filename = "%s.txt" % (name, )
    with open(filename, "w") as f:
        for i in range(0, m):
            f.write("%d %d\n" % (i, sequence(i))) 
