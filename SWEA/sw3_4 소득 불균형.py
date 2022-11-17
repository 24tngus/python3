T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 정수의 개수 
    data = list(map(int, input().split()))
    answer = 0; num = 0

    # 평균 구하기 
    for i in data:
        num += i

    ave = num / N

    # 평균 이하 사람의 수 구하기

    for i in data:
        if i <= ave:
            answer += 1

    print("#{} {}". format(test_case, answer))