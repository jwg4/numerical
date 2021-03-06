import os


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
    if hasattr(sequence, "start"):
        start = sequence.start
    else:
        start = 0
    filename = "%s.txt" % (name,)
    filepath = os.path.join("output", filename)
    with open(filepath, "w") as f:
        for i in range(start, m + 1):
            f.write("%d %d\n" % (i, sequence(i)))
