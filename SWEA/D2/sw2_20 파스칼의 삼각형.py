T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(i+1):
            if j==0 or j==i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j]+arr[i-1][j-1]

    print("#{} ".format(test_case))
    for line in arr:
        answer = [x for x in line if x] # 0 제외하고 출력 
        print(*answer) # [] 제외하고 출력 
