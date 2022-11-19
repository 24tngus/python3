T = 10

for test_case in range(1, T+1):
    N, pw = map(str, input().split())
    stack = []
    answer = ''

    for i in pw:
        n = len(stack)
        
        if n >=1 : 
            if i == stack[n-1]: # 입력할 값과 stack의 마지막 값 비교
                stack.pop() # 같을 경우 삭제
            else:
                stack.append(i) # 같지 않을 경우 추가 
        else:
            stack.append(i) # 첫번째 값은 바로 stack에 저장

    answer = ''.join(stack)

    print("#{} {}". format(test_case, answer))