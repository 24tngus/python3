T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split()) # n개의 뿔, m마리 짐승
    answer = 0

    # a = 유니콘의 수 b = 트윈혼의 수
    # a + b = m (짐승의 수)
    # a + 2b = n (뿔의 개수)

    b = n - m
    a = m - b

    print("#{} {} {}". format(test_case, a, b))