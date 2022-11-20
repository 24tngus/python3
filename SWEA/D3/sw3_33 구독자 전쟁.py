T = int(input())

for test_case in range(1, T+1):
    N, A, B = map(int, input().split()) # N명 사람, P채널 구독 A명, T채널 구독 B명
    max_v = 0; min_v = 0;

    if N < A+B:
        min_v = A + B - N
        
    if A > B:
        max_v = B
    elif A < B:
        max_v = A
    elif A == B:
        max_v = A

    print("#{} {} {}". format(test_case, max_v, min_v))