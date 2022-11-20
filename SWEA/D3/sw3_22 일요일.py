T = int(input())

week = {"MON":1, "TUE":2, "WED":3, "THU":4, "FRI":5, "SAT":6, "SUN":7}

for test_case in range(1, T+1):
    word = input()
    answer = 0

    if word == "SUN":
        answer = week[word]
    else:
        answer = week['SUN'] - week[word]

    print("#{} {}". format(test_case, answer))