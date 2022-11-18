T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 학생의 수 

    answer = N//3

    print("#{} {}". format(test_case, answer))
