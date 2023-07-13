T = int(input())

for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    arr_M = list(map(int, input().split()))
    # K = 한 번 충전으로 최대한 이동할 수 있는 정류장 수 
    # N = 정류장 수 
    # M = 충전기가 설치된 정류장 번호 
    answer = 0
    current = 0

    while current + K < N:
        for step in range(K, 0, -1):
            if current+step in arr_M:
                current += step
                answer += 1
                break
        else:
            answer = 0
            break

    print("#{} {}".format(test_case, answer))


