N = int(input())
num = 0

for _ in range(N):
    arr = list(map(int, input().split()))
    
    sum = 0
    
    for i in arr:
        if i % 2 == 1 :
            sum += i
            
    num += 1
    print("#%d %d" % (num, sum))
