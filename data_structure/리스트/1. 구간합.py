T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split()) # N : 정수의 개수, M : 구간의 개수
    arr = list(map(int, input().split()))
    count = 0

    for i in range(M):
        count += arr[i]

    max = min = count

    for i in range(N-M+1):
        count = 0
        for j in range(i, i+M):
            count += arr[j]

        if count > max:
            max = count
        if count < min:
            min = count

    print("#{} {}".format(test_case, max-min))
