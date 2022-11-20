T = int(input())

for test_case in range(1, T+1):
    a, b, c = map(int, input().split()) # 세 변의 길이 
    answer = 0
    
    if a == b:
        answer = c
    elif a == c:
        answer = b
    else:
        answer = a

    print("#{} {}". format(test_case, answer))