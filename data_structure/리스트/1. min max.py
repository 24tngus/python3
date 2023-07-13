T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    arr = list(map(int, input().split()))

    # arr.sort()로 제출 

    for i in range(N): # 버블 정렬 
        for k in range(N):
            for j in range(0, i):
                if arr[j] > arr[j+1]:
                    arr[j],arr[j+1] = arr[j+1],arr[j]

    answer = arr[-1] - arr[0]

    print("#{} {}".format(test_case, answer))
