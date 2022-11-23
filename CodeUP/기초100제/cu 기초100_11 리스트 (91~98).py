#Q. 1 이상한 출석 번호 부르기 (1)
n = int(input())
arr = list(map(int, input().split()))
answer = [0]*23

for i in arr:
    answer[i-1] += 1

for j in range(len(answer)):
    print(answer[j], end=" ")

#Q. 2 이상한 출석 번호 부르기 (2)
n = int(input())
arr = list(map(int, input().split()))

for i in range(n-1, -1, -1): # (1) for문 사용해 출력
    print(arr[i], end=" ")

print(*arr[::-1]) # (2) 배열 역순 출력
 
#Q. 3 이상한 출석 번호 부르기 (3)
n = int(input())
arr = list(map(int, input().split()))

print(min(arr))

#Q. 4 바둑판에 흰 돌 놓기
n = int(input()) # 흰 돌 개수
board = [[0] * 19 for _ in range(19)] # 19X19 배열 바둑판

for i in range(n):
    a, b = map(int, input().split()) # 흰 돌 좌표 
    if board[a-1][b-1] == 1: # 이미 흰돌이 놓인 경우 
        continue
    else:
        board[a-1][b-1] += 1

for line in board:
    print(*line)

#Q. 5 바둑알 십자 뒤집기
board = [list(map(int, input().split())) for _ in range(19)]
n = int(input()) # 십자 뒤집기 횟수

for i in range(n):
    a, b = map(int, input().split()) # 십자 뒤집기 좌표
    for j in range(19):
        if board[a-1][j] == 0: # 가로줄 바꾸기 
            board[a-1][j] = 1
        else:
            board[a-1][j] = 0

        if board[j][b-1] == 0: # 세로줄 바꾸기
            board[j][b-1] = 1
        else:
            board[j][b-1] = 0

for line in board:
    print(*line)

#Q. 6 설탕과자 뽑기
h, w = map(int, input().split()) # 격자판 세로, 가로
n = int(input()) # 줄에 놓을 수 있는 막대 개수

board = [[0]*w for _ in range(h)] # 격자판

for i in range(1, n+1):
    l, d, x, y = map(int, input().split()) # 막대 길이, 방향, 좌표
    for j in range(l):
        if d == 0: # 가로
            board[x-1][y-1+j] = 1
        else:
            board[x-1+j][y-1] = 1

for line in board:
    print(*line)

#Q. 7 성실한 개미
board = [list(map(int, input().split())) for _ in range(10)] # 10X10 미로 상자
answer = 0 
# (2,2)에서 시작, 방향은 오른쪽 -> 아래쪽
x = 1; y = 1
board[x][y] = 9

for i in range(20):
    if board[x][y+1] == 0: # 오른쪽 이동
        y += 1
    elif board[x+1][y] == 0: # 아래 이동 
        x += 1
    elif board[x][y+1] == 2: # 먹이 찾기 
        board[x][y+1] = 9
        break
    elif board[x+1][y] == 2: 
        board[x+1][y] = 9
        break

    board[x][y] = 9

    if x == 10 or y == 10: # 범위를 벗어날 경우 
        break

for line in board:
    print(*line)
