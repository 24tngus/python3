T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 달팽이 크기 
    arr = [[0 for _ in range(N)] for _ in range(N)] # 달팽이 숫자 배열

    stock = 0 # cycle 마다 축적된 sum의 값

    for i in range(N//2): # 짝수는 딱 떨어지고, 홀수는 1번 부족하게
        cycle = ((N-1)-2*i)

        for j in range(cycle):
            arr[i][i + j] = stock + j+1
            arr[i + j][(N-1)-i] = stock + (cycle)+(j+1)
            arr[(N-1)-i][(N-1)-(i + j)] = stock + 2*(cycle)+(j+1)
            arr[(N-1)-(i + j)][i] = stock + 3*(cycle)+(j+1)
        stock += 4 * cycle # 사이클 마지막 값을 다음 시작점에 더함

    if N % 2 == 1: # 홀수일 경우 
        arr[N//2][N//2] = N**2 # NXN행렬 가운데에 N의 제곱 저장

    print(f'#{test_case}')

    for lines in range(len(arr)): # 각 라인 출력
        print(*arr[lines])
