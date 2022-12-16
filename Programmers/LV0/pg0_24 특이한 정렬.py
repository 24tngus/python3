#Q. 특이한 정렬

# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 
# 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
# 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numlist, n):
    answer = []
    
    # 정수-n의 절댓값 기준으로 정렬하고, 같은 정수라면 내림차순 정렬 
    answer = sorted(numlist, key = lambda a: (abs(a-n), -a))
    
    return answer
