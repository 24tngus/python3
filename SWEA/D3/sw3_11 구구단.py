T = int(input())

for test_case in range(1, T+1):
    A, B = map(int, input().split())
    answer = 0

    if A < 10 and B < 10:
        answer = A * B
    else:
        answer = -1

    print("#{} {}". format(test_case, answer))
