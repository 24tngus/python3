T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # N개의 확률
    answer = 0

    for i in range(N):
        p, x = map(float, input().split())

    print("#%d %.6f"%(test_case, answer))
