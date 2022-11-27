#Q. 컨트롤제트

# 숫자들이 공백으로 구분된 문자열이 주어집니다. 
# 문자열에 있는 숫자를 차례대로 더하려고 합니다. 
# 이 때 “Z”가 나오면 바로 전에 더했던 숫자를 뺀다는 뜻입니다. 
# 숫자와 “Z”로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 하도록 solution 함수를 완성해보세요.


def solution(s):
    answer = 0
    
    num = list(s.split()) # 공백 제거하고 리스트에 저장
    stack = []
    
    for i in num:
        if i == "Z":
            stack.pop()
        else:
            stack.append(i)
            
    for j in stack:
        answer += int(j)

    return answer

    # 10개 중에 2개 테스트케이스가 계속 오류
    '''
    def solution(s):
    answer = 0
    
    num = list(s.split()) # 공백 제거하고 리스트에 저장
    
    for i in range(len(num)):
        if num[i] == "Z":
            if num[i]=="Z" and num[i-1]=='Z': # 지울 숫자가 없는 상태의 Z일 경우
                continue
            else:
                answer -= int(num[i-1])
        else:
            answer += int(num[i])

    return answer
    '''
