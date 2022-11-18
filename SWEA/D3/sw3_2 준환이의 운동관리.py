T = int(input())

for test_case in range(1, T+1):
    L, U, X = map(int, input().split())
    # L분 이상 U분 이하 운동 목표
    # X분만큼 운동 실천 
    answer = 0 

    if X > U: # 더 많은 운동한 경우 -1 출력
        answer = -1
    elif L > X: # 추가로 운동해야 하는 경우 추가 시간 출력
        answer = L-X
    elif L <= X and X <= U: # 목표 만큼 운동한 경우 0 출력
        answer = 0

    print("#{} {}". format(test_case, answer))
