T = int(input())

for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    answer = 0

    data.sort()
    answer = data[-1]

    print("#%d %d" %(test_case, answer))
