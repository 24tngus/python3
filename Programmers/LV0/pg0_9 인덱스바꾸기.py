#Q. 인덱스 바꾸기 

def solution(my_string, num1, num2):
    answer = ''
    
    my_list = list(my_string)
    
    # swap
    my_list[num1],my_list[num2] = my_list[num2],my_list[num1]
    answer = ''.join(my_list)
    return answer
