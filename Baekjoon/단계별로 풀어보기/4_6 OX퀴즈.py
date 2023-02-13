# Q. OX퀴즈

N = int(input())

for _ in range(N):
    arr = list(input())
    score = 0
    sum_score = 0
    for i in arr:
        if i == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)
