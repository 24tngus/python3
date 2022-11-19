T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split()) # N = 수강생의 수, K = 과제 제출한 사람의 수
    num = list(map(int, input().split())) # 과제 제출한 사람의 번호
    answer = [] # 과제 제출하지 않은 사람의 번호 오름차순 출력

    for i in range(1, N+1):
        if i not in num:
            answer.append(str(i))

    print("#{} {}". format(test_case, *answer))