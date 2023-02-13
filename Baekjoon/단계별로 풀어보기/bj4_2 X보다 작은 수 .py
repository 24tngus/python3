# Q. X보다 작은 수 

N, X = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(N):
    if arr[i] < X:
        print(arr[i], end=" ")
