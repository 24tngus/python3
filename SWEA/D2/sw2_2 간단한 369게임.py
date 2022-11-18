T = int(input())
result = ''

for i in range(1, T+1): # 1부터 입력 숫자까지 반복 
    N = str(i)
    N_cnt = 0

    # 3, 6, 9 개수 찾기 
    if '3' in N :
        N_cnt += N.count('3')
    if '6' in N :
        N_cnt += N.count('6')
    if '9' in N :
        N_cnt += N.count('9')

    if N_cnt == 0:
        result += N
    else:
        for j in range(N_cnt): # 3,6,9 개수만큼 - 출력 
            result += '-'
    result += ' ' # 문자열에 공백 추가 
    
print(result)

