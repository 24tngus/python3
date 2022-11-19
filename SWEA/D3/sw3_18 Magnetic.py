T = 10

for test_case in range(1, T+1):
    N = int(input()) # 100X100 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 0 # 교착상태 개수 
    # N극 = 1 # S극 = 2

    for i in range(N): # 세로 별로 1->2 순서 확인 
        stack = []
        for j in range(N):
            if not stack and arr[j][i] == 1: # 스택이 비어있고, 1이 나오면 stack에 넣음
                stack.append(1)
            elif stack and arr[j][i] == 2: # 스택에 1이 있고, 2가 나오면 카운트 1증가
                answer += stack.pop()
       
    print("#{} {}". format(test_case, answer))