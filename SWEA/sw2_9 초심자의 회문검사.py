T = int(input())

for test_case in range(1, T+1):
    data = input().replace(' ', '') # 공백 제거 
    
    answer = 0; ans = 0

    for i in range(len(data)//2):
        if(data == data[::-1]): # 문자열과 거꾸로 문자열 만든 것과 같은지 비교 
            answer = 1
        else:
            answer = 0
    
    print("#{} {}".format(test_case, answer))

# 10개 중에 9개만 맞고 계속 fail 이라서 다른 풀이
'''
for test_case in range(1, T+1):
    data = list(input().replace(' ', '')) # 공백 제거 후 리스트 변환 
    
    answer = 0; ans = 0
    n = len(data)

    for i in range(n//2+1):
        if(data[i]==data[(n-1)-i]):
            ans += 1
        
    if ans >= (n//2):
       	answer = 1
    else:
        answer = 0
    
    print("#{} {}".format(test_case, answer))
'''