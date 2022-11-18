T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    result = []
    
    for i in range(N):
        data, count = input().split()

        for j in range(int(count)):
            result.append(data)

    print("#{}".format(test_case))

    for i in range(len(result)):
        if (i+1) % 10 == 0:
            print(result[i])
        else:
            print(result[i], end='')
    print()
