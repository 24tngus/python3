#Q. 제곱수 판별하기 

import math

def solution(n):
    answer = 0
    
    # 1) *0.5 = 제곱근
    if (n**0.5).is_integer(): # 0.5제곱은 제곱근
        answer = 1
    else:
        answer = 2

    # 2) sqrt() 제곱근 함수 사용
    if math.sqrt(n).is_integer(): # 제곱근 한 후 정수인지 판별 
        answer = 1
    else:
        answer = 2
    return answer