#Q. 1 정수 입력받아 참 거짓 평가하기
a = int(input())
print(bool(a)) # bool함수 : 0일 경우 False, 그 외 True

#Q. 2 참 거짓 바꾸기
a = bool(int(input()))
print(not a)

#Q. 3 둘 다 참일 경우만 참 출력하기
a, b = map(int, input().split())
print(bool(a) and bool(b))

#Q. 4 하나라도 참이면 참 출력하기
a, b = map(int, input().split())
print(bool(a) or bool(b))

#Q. 5 참/거짓이 서로 다를 때에만 참 출력하기
a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print(a and (not b) or (not a) and b)

#Q. 6 참/거짓이 서로 같을 때에만 참 출력하기
a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print((a and b) or ((not a) and (not b)))

#Q. 7 둘 다 거짓일 경우만 참 출력하기
a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print((not a) and (not b))

#Q. 8 비트단위로 NOT 하여 출력하기
a = int(input())
print(~a)

#Q. 9 비트단위로 AND 하여 출력하기
a, b = map(int, input().split())
print(a & b)

#Q. 10 비트단위로 OR 하여 출력하기
a, b = map(int, input().split())
print(a | b)

#Q. 11 비트단위로 XOR 하여 출력하기
a, b = map(int, input().split())
print(a ^ b)