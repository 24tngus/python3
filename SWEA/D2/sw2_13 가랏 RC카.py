
for test_case in range(1, T+1):
    N = int(input()) # Command의 수
    answer = 0 # 카의 이동 거리 
    num = 0 # 현재 RC카의 속도 

    # Command + 가속도의 값
    # 0 : 현재 속도 유지.
    # 1 : 가속
    # 2 : 감속 

    for i in range(N):
        com = list(map(int, input().split()))

        if com[0] == 1:
            num += com[1]
        elif com[0]== 2:
            num -= com[1]

        if num >= 0:
            answer += num
        else: # 속도가 음수일 경우 속도 0으로 유지 
            num = 0

    print("#{} {}".format(test_case, answer))
        
