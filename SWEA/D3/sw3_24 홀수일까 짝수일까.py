T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    answer = ''

    if N % 2 == 0:  # 짝수일 경우
        answer = "Even"

    else:  # 홀수일 경우
        answer = "Odd"

    print("#{} {}".format(test_case, answer))