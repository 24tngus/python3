N = int(input())
num369 = ['3', '6', '9']

for n in range(1, N+1):
    
    cnt = 0
    for s in str(n):
        if s in num369:
            cnt += 1
            
    if cnt > 0:
        n = "-" * cnt
        
    print(n, end=" ")