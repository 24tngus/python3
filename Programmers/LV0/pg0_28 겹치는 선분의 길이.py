# Q. 겹치는 선분의 길이
# 세 선분의 시작과 끝 좌표가 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 return 하도록 solution 함수를 완성해보세요.

def solution(lines):
    answer = 0
    arr = [0 for i in range(200)]
    
    for i in lines:
        x, y = map(int, i)
        
        for value in range(x, y):
            arr[value] += 1
            
    for i in arr:
        if i > 1:
            answer += 1
            
    return answer
