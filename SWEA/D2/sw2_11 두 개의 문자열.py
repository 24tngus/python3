T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    answer = 0

    if N == M:
        for i in range(N):
            answer += A[i] * B[i]
    else:
        if N > M: # 기본은 예시처럼 M > N 인 경우임
            N, M = M, N
            A, B = B, A
        
        for i in range(M-N+1): # B
            max = 0
            for j in range(N): # A
                max += A[j] * B[j+i]

            if max > answer:
                answer = max
                
    print("#{} {}".format(test_case, answer))
