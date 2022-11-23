#Q. 제곱수 판별하기 

# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
# 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

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
