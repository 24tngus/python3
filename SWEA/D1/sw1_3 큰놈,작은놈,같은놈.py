T = int(input())

for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    answer = ''

    if data[0] > data[1]:
        answer += '>'
    elif data [0] == data[1]:
        answer += '='
    elif data[1] < data[0]:
        answer += '<'
    
    print("#%d %s" %(test_case, answer))
