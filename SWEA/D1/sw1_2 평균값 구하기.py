T = int(input())

for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    ave = 0
    answer =0

    for i in range(len(data)):
        ave += data[i]
        answer = round(ave/10)

    print("#%d %d" %(test_case, answer))
