#Q. 영수증

X = int(input()) # N = 영수증에 적힌 총 금액
N = int(input()) # X = 영수증에 적힌 물건 종류의 수 

A=0

for i in range(N):
    a,b = map(int, input().split()) # a = 물건의 가격, b = 물건의 개수 
    A += a*b 

if(X==A):
    print("Yes")
else:
    print("No")
