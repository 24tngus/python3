#Q. 빠른 입출력

import sys

N = int(input())

# (1))
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    print(x+y)

# (2))
a = [map(int, sys.stdin.readline().split()) for i in range(N)]

for x, y in a:
    print(x+y)
