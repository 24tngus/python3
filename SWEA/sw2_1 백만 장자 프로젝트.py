T = int(input()) # 테스트 케이스의 수 

for test_case in range(1, T+1):
    N = int(input()) # N일 동안 물건 매매가 예측함
    price = list(map(int, input().split())) # 매매가

    max_price = price[-1] # N번째가 최댓값
    answer = 0

    # 최댓값과 N-1부터 0까지 비교 
    for i in range(N-1, -1, -1):
        if price[i] >= max_price: # 최댓값보다 크거나 같으면 최댓값으로 바꾸기
            max_price = price[i]
        else:
            answer += (max_price - price[i]) 

    print("#%d %d" %(test_case, answer))