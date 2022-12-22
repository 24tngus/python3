T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int, input().split()) # 현미 빵 A원, 단호박 빵 B원, 총 C원
    answer = 0

    if C/A >= C/B :
        answer = int(C/A)
    else:
        answer = int(C/B)

    print("#{} {}".format(test_case, answer))

