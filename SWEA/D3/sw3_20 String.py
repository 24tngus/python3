T = 10

for test_case in range(1, T+1):
    N = int(input()) # 테스트 케이스 번호
    check = str(input()) # 검색하는 문자열
    sen = input() # 문장
    answer = 0

    n = len(check)

    for i in range(len(sen)): # 문장 전체 검사
        if sen[i:i+n] == check: # 검색 문자열 길이만큼 잘라서 비교
            answer += 1
        
    print("#{} {}". format(test_case, answer))