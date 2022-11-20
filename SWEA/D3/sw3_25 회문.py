T = 10

for test_case in range(1, T+1):
    N = int(input()) # 테스트 케이스 번호
    arr = [list(input()) for _ in range(100)] # 100X100 배열
    answer = [] # 가장 긴 회문 길이

    for i in range(100):
        for j in range(100):
            check = []; check2 = []
            # 가로 검사
            for k in range(100-j):
                check += arr[i][j+k]

                if check == check[::-1]: # 회문이면 회문의 길이 저장
                    answer.append(len(check))

            # 세로 검사
            for k in range(100-i):
                check2 += arr[i+k][j]

                if check2 == check2[::-1]: # 회문이면 회문의 길이 저장
                    answer.append(len(check2))

    print("#{} {}". format(test_case, max(answer)))