for test_case in range(1, 10):
    N = int(input()) # 회문 길이 
    arr = [input() for _ in range(8)] # 8X8 배열 
    answer = 0 # 회문 개수 
    
    # 가로 확인 
    for i in range(8):
        for j in range(8-N+1):
            arr1 = []
            for k in range(N):
                arr1 += arr[i][j+k]
                
                # 회문인지 확인 (배열과 역순 배열이 일치하는지)
            if arr1 == arr1[::-1]:
                answer += 1

        # 세로 확인 
    for i in range(8):
        for j in range(8-N+1):
            arr2 = []
            for k in range(N):
                arr2 += arr[j+k][i]

            if arr2 == arr2[::-1]:
                answer += 1
        
    print("#{} {}". format(test_case, answer))
