# Q. 1 정수 2개 입력받아 합 계산하기 
a, b = map(int, input().split())
print(a+b)

#Q. 2 실수 2개 입력받아 합 계산하기
a = float(input())
b = float(input())
print(a+b)

#Q. 3 10진 정수 입력받아 16진수로 출력하기 (1)
a = int(input())
print('%x'%a)       # %x (16진수 소문자), %o (8진수 소문자)

#Q. 4 10진 정수 입력받아 16진수로 출력하기 (2)
a = int(input())
print('%X'%a)       # %X (16진수 대문자), %O (8진수 대문자)

#Q. 5 16진 정수 입력받아 8진수로 출력하기
a = int(input(), 16) # 16진수 -> 10진수 변환
print('%o'%a)

#Q. 6 영문자 1개 입력받아 10진수로 변환하기
a = input()
print(ord(a))       # 문자 -> 10진수 유니코드 값으로 변환

#Q. 7 정수 입력받아 유니코드 문자로 변환하기
a = int(input())
print(chr(a))       # 10진수 정수 -> 유니코드 문자 변환 
