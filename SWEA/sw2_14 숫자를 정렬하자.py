T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    answer = ''

    data.sort() # 데이터 정렬
    
    for i in data:
        answer += str(i)
        answer += ' '

    print("#{} {}".format(test_case, answer))