hour, min = map(int, input().split())
time = int(input())

plus_hour = time//60 # 몫 = 시
plus_min = time%60   # 나머지 = 분

if plus_min+time>60:
    print(hour+1, plus_min+time-60)
