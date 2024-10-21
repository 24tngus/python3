N = int(input())

num = 1

for _ in range(N):
    max = 0
    arr = list(map(int, input().split()))
    
    for i in arr:
        if i > max:
            max = i
            
    print("#%d %d" %(num, max))
    
    num += 1