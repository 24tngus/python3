T = 10
for test_case in range(1, T + 1):
    N = int(input())  # 평탄화 작업 횟수 제한
    height = list(map(int, input().split()))  # 상자의 높이값
    answer = 0  # 상자의 높이 최고점-최저점

    for i in range(N):  # 작업 횟수만큼 반복
        height.sort()
        height[-1] -= 1
        height[0] += 1

        if height[-1] - height[0] <= 1:  # 횟수 내에 flat 해지면 종료
            break
            
    height.sort()

    answer = height[-1] - height[0]

    print("#{} {}".format(test_case, answer))