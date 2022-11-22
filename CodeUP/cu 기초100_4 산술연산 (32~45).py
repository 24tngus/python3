#Q. 1 정수 1개 입력받아 부호 바꾸기
a = int(input())
print(-a)

#Q. 2 문자 1개 입력받아 다음 문자 출력하기
a = input()
b = ord(a)+1
print(chr(b))

#Q. 3 정수 2개 입력받아 차 계산하기
a, b = map(int, input().split())
print(a-b)

#Q. 4 실수 2개 입력받아 곱 계산하기
a, b = map(float, input().split())
print(a*b)

#Q. 5 단어 여러 번 출력하기
a, n = input().split() 
print(a * int(n)) # n번 반복 

#Q. 6 문장 여러 번 출력하기
n = input()
a = input()
print(a * int(n))

#Q. 7 정수 2개 입력받아 거듭제곱 계산하기
a, b = map(int, input().split())
print(a**b) # a를 b번 곱한 거듭제곱 

#Q. 8 실수 2개 입력받아 거듭제곱 계산하기
a, b = map(float, input().split())
print(a**b)

#Q. 9 정수 2개 입력받아 나눈 몫 계산하기
a, b = map(int, input().split())
print(a//b)

#Q. 10 정수 2개 입력받아 나눈 나머지 계산하기
a, b = map(int, input().split())
print(a%b)

#Q. 11 실수 1개 입력받아 소숫점이하 자리 변환하기
a = float(input())
print(format(a, ".2f"))
print(round(a, 2))     # round함수 (정수로 나눠질 경우 소수점 1자리 밖에 안나옴)

#Q. 12 실수 2개 입력받아 나눈 결과 계산하기
a, b = map(float, input().split())
print(format(a/b, ".3f"))

#Q. 13 정수 2개 입력받아 자동 계산하기
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b, ".2f"))

#Q. 14 정수 3개 입력받아 합과 평균 출력하기
a, b, c = map(int, input().split())
sum = a+b+c
ave = sum/3
print(sum, format(ave, ".2f"))
