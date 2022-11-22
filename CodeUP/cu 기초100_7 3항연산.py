#Q. 1 정수 2개 입력받아 큰 값 출력하기
a, b = map(int, input().split())
c = a if a>=b else b
print(c)

#Q. 2 정수 3개 입력받아 가장 작은 값 출력하기
a, b, c = map(int, input().split())

min = (b if a>b else a) if ((b if a>b else a)<c) else c

if a > b:
    if b > c: 
        min = c
    else: 
        min = b
else: 
    if a > c:
        min = c
    else:
        min = a
print(min)