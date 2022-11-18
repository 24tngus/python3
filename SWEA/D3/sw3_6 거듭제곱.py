for i in range(10):
    T = int(input())
    N, M = map(int, input().split())
    answer = 1

    for j in range(M):
        answer *= N

    print("#{} {}". format(T, answer))
