N = int(input())
num = 1

for _ in range(N):
    n = int(input())
    arr = list(map(int, input().split()))
    sum = 0
    max = 0
    
    for a in arr[::-1]:
        if (a >= max):
            max = a
        else:
            sum += max - a
    
    print("#%d %d" %(num, sum))
    num += 1