#Q. 1 정수 3개 입력받아 짝수만 출력하기
a, b, c = map(int, input().split())

for i in [a, b, c]:
    if i % 2 == 0:
        print(i)

#Q. 2 정수 3개 입력받아 짝/홀 출력하기
a, b, c = map(int, input().split())

for i in [a, b, c]:
    if i % 2 == 0:
        print("even")
    else:
        print("odd")
 
#Q. 3 정수 1개 입력받아 분류하기
a = int(input())

if a < 0 :
    if a % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if a % 2 == 0:
        print("C")
    else:
        print("D")

#Q. 4 점수 입력받아 평가 출력하기
a = int(input())

if a >= 90:
    print("A")
elif a < 90 and a >= 70:
    print("B")
elif a < 70 and a>= 40:
    print("C")
else:
    print("D")

#Q. 5 평가 입력받아 다르게 출력하기
a = input()

if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

#Q. 6 월 입력받아 계절 출력하기
a = int(input())

if a in [12, 1, 2]:
    print("winter")
elif a in [3, 4, 5]:
    print("spring")
elif a in [6, 7, 8]:
    print("summer")
elif a in [9, 10, 11]:
    print("fall")

