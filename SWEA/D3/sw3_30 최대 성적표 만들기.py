T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split()) # N개의 과목 중 K개 선택
    score = list(map(int, input().split())) 
    answer = 0 # 성적표 최대 총점 

    score.sort() # 정렬

    for i in range(1,K+1):
        answer += score[-i]

    print("#{} {}". format(test_case, answer))