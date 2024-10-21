N = int(input())
num = 1

for _ in range(N):
    a, b = map(int, input().split())
    
    m = a / b
    n = a % b
    
    print("#%d %d %d" %(num, m, n))
    num += 1