T = int(input()) # 테스트 케이스 개수 

for test_case in range(1, T+1):
    data = input()

    for i in range(1,10): # 문자열 길이 30 (마디 최대길이 10)
        if data[ : i] == data[i : i*2]:
            # print(data[:i]) 문자열 확인 
            print("#%d %d" %(test_case, i))
            break