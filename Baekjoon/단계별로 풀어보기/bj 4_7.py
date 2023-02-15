# Q. 평균은 넘겠지 

C = int(input())

for _ in range(C):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:]) / arr[0]

    N = 0
    for i in arr[1:]:
        if i > avg:
            N += 1

    answer = (N / arr[0]) * 100
    print('%.3f'% answer + '%')