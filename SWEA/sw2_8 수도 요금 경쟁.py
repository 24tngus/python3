T = int(input()) 

for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    # P : 1L당 요금
    # Q : R리터 이하 요금 (기본요금)
    # S : 추가 1L당 요금
    # W : 한 달간 사용하는 수도의 양

    answer = 0

    if(R < W):
        W_A = P * W
        W_B = Q + (W-R) * S
    else:
        W_A = P * W
        W_B = Q 

    if W_A > W_B:
        answer = W_B
    else:
        answer = W_A

    print("#{} {}".format(test_case, answer))