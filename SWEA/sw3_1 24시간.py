T = int(input())

for test_case in range(1, T+1):
    A, B = map(int, input().split())

    answer = A + B

    if A+B >= 24:
        answer = answer % 24

    print("#{} {}". format(test_case, answer))