with open('rosalind_lcsm.txt', 'r') as file:
    k = []   # k = DNA strings
    lst = file.read().split('>')[1:] 
    
    for i in range(len(lst)):
        new = lst[i].split('\n', 1)
        seq = new[1].replace('\n', '')
        k.append(seq)
def LCSM():
    longest_common_substring = ''
    shortest_string = min(k, key=len)
    
    for i in range(len(shortest_string)):
        for j in range(i, len(shortest_string)+1):
            poss_string = shortest_string[i:j]
            if len(poss_string) > len(longest_common_substring) and all(poss_string in string for string in k):
                longest_common_substring = poss_string
                
    print(longest_common_substring)
LCSM()
