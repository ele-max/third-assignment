from itertools import product
data = open('rosalind_lexf.txt','r').readlines()
alphabet = data[0].split()
n = int(data[1])
    
def lexf(alphabet,n):
    S = product(alphabet, repeat = n)
    for i in S:
        print (''.join(i))
    
lexf(alphabet,n)