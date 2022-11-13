#Q. 가장 큰 수 찾기 

def solution(array):
    answer = [0,0]
    
    answer[0] = max(array) # 가장 큰 수 
    answer[1] = array.index(max(array)) # 큰 수의 위치
    
    return answer