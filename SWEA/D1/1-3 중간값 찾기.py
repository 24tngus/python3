N = int(input())

arr = list(map(int, input().split()))
        
arr.sort()

i = round(N/2) - 1

print(arr[i])