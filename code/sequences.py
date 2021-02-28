from a002405 import *
from oeis import bfile, more


if __name__ == "__main__":
    sequences = [
        A002398,
        A002399,
        A002400,
        A002401,
        A002402,
        A002403,
        A002404,
        A002405,
        A002406,
    ]
    for sequence in sequences:
        print(sequence.__name__)
        print(more(sequence))
        bfile(sequence, 100)
