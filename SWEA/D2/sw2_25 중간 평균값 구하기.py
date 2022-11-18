T = int(input())

for test_case in range(1, T+1):
    data = list(map(int, input().split()))
    num = 0 # 나머지 수 모두 더한 합 

    data.sort() # 정렬
    
    for i in range(1,9): # 최대 수와 최소 수 제외
        num += data[i]

    answer = round(num/8)

    print("#{} {}".format(test_case, answer))

