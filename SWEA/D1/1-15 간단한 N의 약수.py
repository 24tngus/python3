N = int(input())
i = 1

for _ in range(N):
    if (N % i == 0):
        print(i, end = " ")
    i += 1
    