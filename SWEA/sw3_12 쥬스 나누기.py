T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    print("#{} ". format(test_case), end='')

    for i in range(N):
        print("{}/{} ". format(1, N), end='')
    print()