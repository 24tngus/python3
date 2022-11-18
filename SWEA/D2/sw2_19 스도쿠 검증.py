T = int(input())

for test_case in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)] # 스도쿠는 9 X 9 배열 
    answer = 1

    for i in range(9): 
        arr1 = [0] * 10 # 세로 확인 배열
        arr2 = [0] * 10 # 가로 확인 배열

        for j in range(9):
            arr1[sudoku[j][i]] += 1 # 세로 배열 확인
            arr2[sudoku[i][j]] += 1 # 가로 배열 확인

        for k in range(1, 10):
            if arr1[k] != 1:
                answer = 0
                break
            if arr2[k] != 1:
                answer = 0
                break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            arr3 = [0] * 10 # 3X3 확인 배열 
            
            for a in range(3):
                for b in range(3):
                    arr3[sudoku[i+a][j+b]] += 1 # 3X3 배열 확인 

            for k in range(1,10):
                if arr3[k] != 1:
                    answer = 0
                    break

    print("#{} {}".format(test_case, answer))
