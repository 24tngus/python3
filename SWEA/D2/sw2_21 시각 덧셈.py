T = int(input())

for test_case in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())

    hour = h1 + h2
    min = m1 + m2

    if min >= 60:
        hour += 1
        min -= 60

    if hour > 12:
        hour -= 12

    print("#{} {} {}".format(test_case, hour, min)) 

