#Q. 문자열 정렬하기 

def solution(my_string):
    answer = []
    
    for i in my_string:
        if i.isdigit(): # 0~9 숫자 있는지 확인 
            answer.append(int(i)) 
    answer.sort()
    
    return answer
