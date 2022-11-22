#Q. 1 정수 1개 입력받아 2배 곱해 출력하기
a = int(input())
print(a<<1) # 2배 곱하기

#Q. 2 2의 거듭제곱 배로 곱해 출력하기
a, b = map(int, input().split())
print(a<<b)

#Q. 3 정수 2개 입력받아 비교하기 (1)
a, b = map(int, input().split())
if a<b:
    print("True")
else:
    print("False")

#Q. 4 정수 2개 입력받아 비교하기 (2)
a, b = map(int, input().split())
if a == b:
    print("True")
else:
    print("False")

#Q. 5 정수 2개 입력받아 비교하기 (3)
a, b = map(int, input().split())
if a <= b:
    print("True")
else:
    print("False")

#Q. 6 정수 2개 입력받아 비교하기 (4)
a, b = map(int, input().split())
if a != b:
    print("True")
else:
    print("False")
