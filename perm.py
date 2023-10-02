import itertools
from itertools import permutations

def PERM(n):
    k = range(1, n+1)
    perm = list(itertools.permutations(k, n))
    print(len(perm))
    for i in perm:
        print(*i)
with open('rosalind_perm.txt', 'r') as f:
    f = f.readline()
    n = int(f[0])
PERM(n)