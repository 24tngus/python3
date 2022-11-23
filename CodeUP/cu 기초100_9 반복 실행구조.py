#Q. 1 0 입력될 때까지 무한 출력하기
n = 1
while n != 0:
    n = int(input())

    if n != 0:
        print(n)
    else:
        break

#Q. 2 정수 1개 입력받아 카운트다운 출력하기 (1)
n = int(input())

while n != 0:
    if n == 0:
        break
    else:
        print(n)
        n -= 1

#Q. 3 정수 1개 입력받아 카운트다운 출력하기 (2)
n = int(input())

while n != 0:
    if n == 0:
        print(n)
        break
    else:
        n -= 1
        print(n)

#Q. 4 문자 1개 입력받아 알파벳 출력하기
n = ord(input()) # 10진 아스키코드 정수로 변환
a = ord('a')

while a <= n:
    print(chr(a), end=" ")
    a += 1

#Q. 5 정수 1개 입력받아 그 수까지 출력하기 (1)
a = int(input())
b = int(0)

while b <= a:
    print(b)
    b += 1
    
#Q. 6 정수 1개 입력받아 그 수까지 출력하기 (2)
a = int(input())

for i in range(a+1):
    print(i)