T = int(input())

for test_case in range(1, T+1):
    answer = "Yes"
    S = input()

    for i in S:
        if S.count(i) != 2:
            answer = "No"

    print("#{} {}".format(test_case, answer))