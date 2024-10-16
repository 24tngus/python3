N = int(input())
num = 0

for _ in range(N):
    arr = list(map(int, input().split()))
    
    sum = 0
    
    for i in arr:
        sum += i
            
    sum = round(sum / 10)
            
    num += 1
    print("#%d %d" % (num, sum))
