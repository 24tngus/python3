T = int(input()) 

for test_case in range(1, T+1):
    N = int(input()) # 테스트 케이스 번호 
    score = list(map(int, input().split())) # 1000개의 점수
    data = [0] * 1001
    answer = []

    for i in score:  # 각 숫자가 몇개 있는지 저장하는 배열 
        data[i] += 1

    val = max(data) # 가장 많이 있는 숫자의 최대 개수 

    for j in range(len(data)): # 가장 많이 있는 숫자가 뭔지 찾기
        if data[j] == val:
            answer.append(j)

    print("#{} {}".format(N, max(answer)))

    
