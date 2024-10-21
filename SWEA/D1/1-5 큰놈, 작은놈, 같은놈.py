N = int(input())
num = 1

for _ in range(N):
    arr = list(map(int, input().split()))
 
    if arr[0] > arr[1]:
        print("#%d" %num, ">")
    elif arr[0] == arr[1]:
        print("#%d" %num, "=")
    elif arr[0] < arr[1]:
        print("#%d" %num, "<")
    
    num += 1