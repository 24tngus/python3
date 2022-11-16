T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # N의 배수 번호 
    num = []
    count = 0
    N_num = N # N의 배수 담을 변수 
    
    while(len(num) != 10): # 집합에 0~9까지 들어가면 총 10이 됨
        count += 1 # 몇 번째 
        N_num = N * count  
        
        for i in str(N_num):
            if i in num:
                continue
            else:
                num.append(i)
                num.sort()
               
    print("#{} {}".format(test_case, N*count))

# 집합으로 할 경우 '제한시간 초과' 나옴 
'''
for test_case in range(1, T+1):
    N = int(input()) # N의 배수 번호 
    s = set() # 중복 제거된 집합set 선언 
    count = 0
    N_num = N # 배수 담을 변수 

    while len(s) != 10: # 집합에 0~9까지 들어가면 총 10이 됨
        count += 1 # 몇번 양을 세었는지
        N_num = N * count

        for i in str(N):
            s.add(i)
           
    print("#{} {}".format(test_case, N*count))
'''

