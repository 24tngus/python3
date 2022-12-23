T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))
    answer = [[0] for i in range(N)]
    n = 0

    if N % 2 == 0:
        card_L = card[:int(N/2)]
        card_R = card[int(N/2):]
    else:
        card_L = card[:int(N/2)+1]
        card_R = card[int(N/2)+1:]

    for i in range(len(card_R)):
        answer[n] = card_L[i]
        answer[n+1] = card_R[i]
        n += 2

    if N%2 == 1:
        answer[n] = card_L[-1]

    answer = " ".join(answer)
    
    print("#{} {}".format(test_case, answer))