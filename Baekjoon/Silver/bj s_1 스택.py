import sys

T = int(input())
stack = []

for test_case in range(1, T+1):
    N = sys.stdin.readline().split()
    com = N[0] # 명령어 확인 

    if com == "push": # 정수 X를 스택에 넣는 연산
        val = N[1]
        stack.append(val) 

    elif com == "pop": # 스택에서 가장 위에 있는 정수를 빼고, 출력
        if len(stack) == 0 :
            print(-1)
        else:
            print(stack.pop())
    
    elif com == "size": # 스택에 들어있는 정수의 개수 출력
        print(len(stack))

    elif com == "empty" : # 스택이 비어있으면 1, 아니면 0 출력
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif com == "top": # 스택의 가장 위에 있는 정수 출력 (없을 경우 -1)
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
