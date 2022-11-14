T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    data = list(map(int, input().split(" "))) # list에 입력 값 저장 
    
    answer=0
    for i in data:
        if data[i] % 2 == 1: # 홀수 찾기 
            answer += data[i] # 홀수 값 더하기 
            
    print("#%d %d", test_case, answer)
                