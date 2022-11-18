#Q. 빠른 입출력

import sys

N = int(input())

# 리스트 사용하지 않을 경우 
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    print(x+y)

# 리스트 사용할 경우 
a = [map(int, sys.stdin.readline().split()) for i in range(N)]

for x, y in a:
    print(x+y)
