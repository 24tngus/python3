T = int(input())

for test_case in range(1, T+1):
    score = list(map(int, input().split()))
    sum = 0

    for i in range(len(score)):
        if score[i] < 40:
            score[i] = 40

        sum += score[i]

    answer = int(sum / 5)

    print("#{} {}". format(test_case, answer))
