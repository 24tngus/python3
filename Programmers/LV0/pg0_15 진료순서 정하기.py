#Q. 진료순서 정하기

# 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 
# 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

import copy

def solution(emergency):
    answer = [0] * len(emergency)
    
    num = copy.deepcopy(emergency)
    num.sort(reverse=True)
    
    for i in range(len(emergency)):
        n = num[i]
        answer[emergency.index(n)] = i + 1
    
    return answer
