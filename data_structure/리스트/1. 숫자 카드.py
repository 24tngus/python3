T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(input())
    num = [0] * 10

    for i in arr: # 숫자별로 개수 저장
        num[int(i)] += 1

    n = max(num)
    answer = [0] * (n+1)

    for i in range(len(num)): # 개수별로 숫자 저장
        answer[num[i]] = i
    
    print("#{} {} {}".format(test_case, answer[-1], len(answer)-1))