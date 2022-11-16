T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # N = 단어 퍼즐의 가로, 세로 길이 (5<=N<=15)
    # K = 단어의 길이 (2<=K<=N)

    answer = 0
    cnt = 0

    for i in range(N):
		# 행 검사 
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N-1: # 0을 만났을 때 cnt 초기화
                if cnt == K:  # 한 행이 끝날 때 cnt값이 K이면 answer += 1
                    answer += 1
                cnt = 0

    	# 열 검사 
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == N-1: # 0을 만났을 때 cnt 초기화 (11001도 k=3일 경우 1이 됨)
                if cnt == K: # 한 열이 끝날 때 cnt값이 K이면 answer += 1
                    answer += 1
                cnt = 0

    print("#{} {}".format(test_case, answer))