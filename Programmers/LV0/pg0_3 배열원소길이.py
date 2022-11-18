#Q. 배열 원소의 길이

def solution(strlist):
    answer = []
    
    # 1) append 이용

    for i in strlist:
        answer.append(len(i))

    # 2) map 함수 이용

    answer = list(map(len, strlist))
    return answer
