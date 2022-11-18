# Q. A+B (출력 포맷팅) 

import sys

T = int(input())

for i in range(T):
    A,B=map(int, sys.stdin.readline().split())  
    print(f'Case #{i+1}: {A} + {B} =', A+B)

    # Case #번호: A+B 출력 
    print("Case #%d:"%(i+1), A+B)  # (1) 
    print(f'Case #{i+1}:', A+B)    # (2)
