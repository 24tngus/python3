# Q. 평행
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

def solution(dots):
    answer = 0
    arr = [[0,0] for i in range(6)]
    n = 0

    # x, y좌표의 차가 같아야 평행 
    for i in range(3):
        for j in range(i+1, 4):
            arr[n][0] += dots[i][0]-dots[j][0]
            arr[n][1] += dots[i][1]-dots[j][1]
            n += 1

    for j in arr:
        if arr.count(j) == 2:
            answer = 1

    return answer
