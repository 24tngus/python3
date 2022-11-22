#Q. 1 문자 입출력
a = input()
print(a)

#Q. 2 정수 입출력
a = int(input())
print(a)

#Q. 3 실수 입출력
a = float(input())
print(a)

#Q. 4 정수 2개 입출력 
a = int(input())
b = int(input())
print(a)
print(b)

#Q. 5 문자 출력 순서 바꾸기 (1)
a = input()
b = input()
print(b)
print(a)

#Q. 6 실수 반복 출력
a = input()
print(a)
print(a)
print(a)

#Q. 7 공백을 두고 입력된 정수 입출력
a, b = map(int, input().split())
print(a)
print(b)

#Q. 8 문자 출력 순서 바꾸기 (2)
a, b = input().split()
print(b, a)

#Q. 9 한 줄로 반복 출력 
a = input()
print(a, a, a)

#Q. 10 :(콜론) 입출력
a, b = input().split(':')
print(a, b, sep=':')             #  구분 기호 sep=""

#Q. 11 구분기호 기준으로 입출력
y, m, d = input().split('.')
print(d, m, y, sep="-")

#Q. 12 구분기호 빼고 입출력
a, b = input().split("-")
print(a, b, sep="")

#Q. 13 문자열을 한 문자씩 출력
a = input()
for i in range(5):
    print(a[i])

#Q. 14 문자열 슬라이싱 입출력 
a = input()
print(a[0:2], a[2:4], a[4:6])

#Q. 15 구분기호 입출력
h, m, s = input().split(':')
print(m)

#Q. 16 문자열 2개 붙여 출력
a, b = input().split()
print(a+b)
