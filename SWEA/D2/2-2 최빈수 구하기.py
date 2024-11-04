N = int(input())

for _ in range(N):
    num = int(input())
    
    arr = list(map(int, input().split()))
    brr = [0] * 101
    max = 0
    
    for a in arr:
        brr[a] += 1
        
        if (brr[a] >= brr[max]):
            max = a
    
    print("#%d %d" %(num, max))
