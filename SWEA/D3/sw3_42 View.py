T = 10

for test_case in range(1, T+1):
    N = int(input()) # 건물의 개수 
    height = list(map(int, input().split())) # 건물의 높이 
    answer = 0 # 조망권 확보된 세대 수 

    for i in range(2, N-1):
        data = height[i-2:i+3]
        data.sort()

        if height[i] == max(data):
            answer += data[-1] - data[-2]

    print("#{} {}".format(test_case, answer))