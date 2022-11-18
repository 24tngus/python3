T = int(input())

month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for test_case in range(1, T+1):
    date = list(map(int, input().split()))
    answer = 0

    if date[0] == date[2]:
        answer = date[3] - date[1] + 1
    else:
        answer += month[int(date[0])]-int(date[1]) + 1 # 시작 월의 날짜 계산
        answer += int(date[3])                 # 끝 월의 날짜 계산
        for i in range(date[0]+1, date[2]): # 사이 월의 날짜 계산
            answer += month[int(i)]

    print("#{} {}".format(test_case, answer))
    

