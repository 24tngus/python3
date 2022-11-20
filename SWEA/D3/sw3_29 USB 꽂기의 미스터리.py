T = int(input())

for test_case in range(1, T+1):
    p, q = map(float, input().split()) 
    # p = 올바른 면으로 USB를 꽂을 확률
    # q = 정상적으로 USB가 꽂힐 확률
    answer = ''

    # 1번 뒤집어서 올바른 면에 꽂고 작동할 확률
    # (처음에 뒤집어서 꽂고, 다음에 제대로 꽂은 경우)
    s1 = (1-p)*q

    # 2번 뒤집어서 올바른 면에 꽂을 확률
    # (처음에 올바른 면&비정상 꽂기, 다음에 뒤집은 면, 마지막 제대로 꽂기)
    s2 = p * (1-q) * q

    if s1 < s2:
        answer = "YES"
    else:
        answer = "NO"

    print("#{} {}". format(test_case, answer))