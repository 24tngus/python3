T = int(input())

for test_case in range(1, T+1):
    A, B = map(int, input().split()) # A이상 B이하 
    answer = 0 # 제곱 팰린드롬 수의 개수 

    for i in range(A, B+1):
        C = i ** (1/2) # 제곱근

        if C == int(C): # 제곱근이 정수일 때
            i = str(i)
            C = str(int(C))
            if i == i[::-1] and C == C[::-1]:
                answer += 1

    print("#{} {}". format(test_case, answer))


# 맞긴 했는데 지저분해서 다시 찾음
'''
for test_case in range(1, T+1):
    A, B = map(int, input().split()) # A이상 B이하 
    answer = 0 # 제곱 팰린드롬 수의 개수 
    arr = []

    for i in range(A, B+1):
        arr = list(str(i))
        if arr == arr[::-1]:
            num = ''.join(arr)
            num = math.sqrt(int(num)) # 제곱근 

            if num.is_integer(): # 제곱근이 정수일 때
                arr = list(str(int(num)))
                print(arr)
                if arr == arr[::-1]:
                    answer += 1
    print("#{} {}". format(test_case, answer))
'''
