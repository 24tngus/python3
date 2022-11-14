T = int(input())
date = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T + 1):
    data = str(input())
    year = data[0:4] # 입력값 중 년도
    month = data[4:6] # 입력값 중 월
    day = data[6:8] # 입력값 중 일

    answer = '' 

    if 0 < int(month) < 13 and 0 < int(day) <= date[int(month)]:
        answer = year + '/' + month + '/' + day
    else:
        answer += '-1'

    print("#%d %s" %(test_case, answer))