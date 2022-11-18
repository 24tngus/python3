T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split()) 
    arr = [list(map(int, input().split())) for _ in range(N)]
    # N = NXN 배열의 크기
    # M = MXM 파리채의 크기 
    num_max = []  # 파리 갯수 최댓값

    for i in range(N-M+1): # 0부터 N-M까지 확인 
        for j in range(N-M+1): # M 개수만큼 더하기 
            num = 0 # 파리 갯수 합 

            for a in range(M): # 파리채 박스안의 값 더하기
                for b in range(M):
                    num += arr[i+a][j+b]
            
            num_max.append(num)
    
    answer = max(num_max)
    print("#{} {}".format(test_case, answer))
