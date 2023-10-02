
def rabbits(n, k):
    
    rabbit = []
    rabbit.append(0)
    rabbit.append(1)
 
    for x in range(1, n):
        
        if x < k:
            rabbit.append(rabbit[x] + rabbit[x-1])
        if x == k:
            rabbit.append(rabbit[x] + rabbit[x-1] - rabbit[x-k+1])
        if x > k:
            rabbit.append(rabbit[x] + rabbit[x-1] - rabbit[x-k])

    return rabbit[n]

print(rabbits(80,19))