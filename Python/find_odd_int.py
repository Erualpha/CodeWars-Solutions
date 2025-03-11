from collections import Counter

def find_it(seq):
    n = Counter(seq)
    for i in n:
        if n[i] % 2 != 0:
            return i
