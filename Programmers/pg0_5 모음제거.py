#Q. 모음 제거 

def solution(my_string):
    answer = ''
    
    vow = ("a,e,i,o,u") # 모음 문자열 생성 
    
    for i in vow:
        my_string = my_string.replace(i, "") # 모음을 공백으로 바꾸기 
        
    answer = my_string
        
    return answer