T = int(input())

data = list(map(int, input().split()))
data.sort()
answer = data[(T-1)//2]

print(answer)

# 계속 런타임 에러나서 for문 빼고 했더니 성공
'''
for test_case in range(1, T + 1): 
    data = list(map(int, input().split()))
    answer = 0

    data.sort()
    answer = data[T//2]

    print(answer)
'''