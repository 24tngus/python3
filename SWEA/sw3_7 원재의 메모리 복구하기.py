T = int(input())

for test_case in range(1, T+1):
    data = input()
    answer = 0
    N = '0'

    for i in range(len(data)):
        if data[i] != N:
            N = data[i]
            answer += 1

    print("#{} {}". format(test_case, answer))