T = int(input()) # 테스트 케이스의 개수 

for test_case in range(1, T+1):
    data = int(input())
    a = 0; b = 0; c = 0; d = 0; e = 0

    while(data != 1):
        if data % 2 == 0:
            a += 1
            data /= 2
        elif data % 3 == 0:
            b += 1
            data /= 3
        elif data % 5 == 0:
            c += 1
            data /= 5
        elif data % 7 == 0:
            d += 1
            data /= 7
        elif data % 11 == 0:
            e += 1
            data /= 11

    print("#{} {} {} {} {} {}".format(test_case, a, b, c, d, e))