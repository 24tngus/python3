T = int(input())

for t in range(1, T+1):
    
    arr = list(map(int, input().split()))
    
    arr.sort()
    minnum = arr[0]
    maxnum = arr[-1]
    arr.remove(minnum)
    arr.remove(maxnum)
    
    answer = round(sum(arr) / len(arr))
       
    print("#%d %d" %(t, answer))