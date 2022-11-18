T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    answer = 0

    for i in range(1, N+1):
        if i%2 == 0: # 짝수일 경우
            answer -= i 
        else: # 홀수일 경우 
            answer += i
    
    print ("#{} {}".format(test_case, answer))
