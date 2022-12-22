T = int(input())

date = {1: 31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for test_case in range(1, T+1):
    m, d = map(int, input().split())
    answer = d

    for i in range(1,m):
        answer += date[i]
        print(i, date[i], answer)

    answer += 3
    answer %= 7

    print("#{} {}".format(test_case, answer))