T = int(input())

score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+' ,'C0' ,'C-' ,'D0']

for test_case in range(1, T+1):
    N, K = map(int, input().split()) # N = 학생수, K = 학점을 알고싶은 학생의 번호 
    data = []
    sum_abc = 0

    for i in range(N):
        a, b, c = map(int, input().split())
        sum_abc = a*0.35 + b*0.45 + c*0.20
        data.append(sum_abc)

    K_value = data[K-1]
    data.sort(reverse=True) # 역순으로 정렬 (큰게 앞으로)

    value = N // 10 # 10보다 클 경우 동일한 평점 
    answer = data.index(K_value) // value

    print("#{} {}".format(test_case, score[answer]))
