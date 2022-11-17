T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    score = [list(map(int, input())) for _ in range(N)]
    answer = 0

    # 중간 이전 (가운데 포함)
    for i in range(N//2+1):
        for j in range(N//2-i,N//2+i+1):
            answer += score[i][j]

    # 중간 이후 
    for i in range(1,N//2+1):
        for j in range(i,N-i):
            answer += score[i+N//2][j]

    print("#{} {}". format(test_case, answer))