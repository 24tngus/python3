T = int(input())

for test_case in range(1, T+1):
    data1, data2 = map(int, input().split())
    
    answer1 = data1//data2
    answer2 = data1%data2
    
    print("#%d %d %d" %(test_case, answer1, answer2))