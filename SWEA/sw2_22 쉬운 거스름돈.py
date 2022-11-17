T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 손님에게 거슬러 줘야 할 금액

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    answer = [0] * 8

    for i in range(8):
        if N // money[i] != 0:
            answer[i] = N //money[i]
            N = N % money[i]

    print("#{}".format(test_case))
    print(*answer)