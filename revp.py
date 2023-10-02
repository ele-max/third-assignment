with open('rosalind_revp.txt', 'r') as file:
    f = file.read()
    lst = f.split('\n', 1)
    seq = list(lst[1].replace('\n', ''))
def REVP(seq):
    nucleotides = [['A', 'T'], ['C', 'G']]
    for x in range(len(seq)):
        for y in range(4, 13, 2):
            if x+y <= len(seq):
                palindrome = seq[x : x+y]
                for z in range(y//2):
                    p = True
                    if sorted([palindrome[z], palindrome[y-z-1]]) not in nucleotides:
                        p = False
                        break
                if p == True:
                    print(x+1, y) 
REVP(seq)