T = int(input())
answer = ''

for i in range(1, T+1):
    if (T % i) == 0:
        print(i, end=' ')
        
# 문자열이나 배열에 담아서 출력하고 싶었는데 
# 문자열은 사이 공백을 못담았고
# 배열은 출력형식과 맞지 않았음
'''
T = int(input())
answer = ''

for i in range(1, T+1):
    if (T % i) == 0:
        answer += str(i)

print(answer)
'''