T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 통나무 길이 
    answer = ''

    if N % 2 ==0:
        answer = 'Alice'
    else:
        answer = "Bob"

    print("#{} {}". format(test_case, answer))