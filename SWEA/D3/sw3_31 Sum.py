T = 10

for test_case in range(1, T+1):
    N = int(input()) # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)] # 100X100 배열
    answer = [] # 각 행의 합, 각 열의 합, 각 대각선의 합 저장

    for i in range(100):
        row = 0; col = 0; dia = 0
        for j in range(100):
            row += int(arr[i][j])
            col += int(arr[j][i])

            if i==j:
                dia + int(arr[i][j])

        answer.append(row)
        answer.append(col)
        answer.append(dia)

    print("#{} {}". format(test_case, max(answer)))