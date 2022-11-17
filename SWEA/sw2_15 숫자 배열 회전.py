T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # N X N 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = []

    # 90, 180, 270 회전할 배열 초기화
    arr_90 = [ [0 for _ in range(N)] for _ in range(N)] # N X N 행렬
    arr_180 = [ [0 for _ in range(N)] for _ in range(N)]
    arr_270 = [ [0 for _ in range(N)] for _ in range(N)]

    # arr 행렬 90도 회전
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N-1-j][i]
    # arr 행렬 180도 회전
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr_90[N-1-j][i] # 90도 행렬을 90도 회전
    # arr 행렬 270도 회전
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr_180[N-1-j][i] # 180도 행렬을 90도 회전

    print("#{} ".format(test_case))
    for i in range(N):
        for a in range(N):
            print(arr_90[i][a], end='')
        print(end=" ")
        for b in range(N):
            print(arr_180[i][b], end='')
        print(end=" ")
        for c in range(N):
            print(arr_270[i][c], end='')
        print( )