#Q. 1 짝수 합 구하기
a = int(input())
sum = 0

for i in range(1, a+1):
    if i % 2 == 0:
        sum += i

print(sum)

#Q. 2 원하는 문자가 입력될 때까지 반복 출력하기
n = 0

while n != "q":
    n = input()

    if n != 'q':
        print(n)
    else:
        print(n)
        break

#Q. 3 언제까지 더해야 할까?
a = int(input())
sum = 0
for i in range(1, a+1):
    sum += i
    if sum >= a:
        print(i)
        break

#Q. 4 주사위 2개 던지기
n, m = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, m+1):
        print(i, j)
#Q. 5 16진수 구구단 출력하기
a = input()
n = int(a, 16) # 16진수를 10진수로 변환

for i in range(1, 16):
    print("%X"%n,"*%X"%i, "=%X"%(n*i), sep="")

#Q. 6 3 6 9 게임의 왕이 되자
a = int(input())
for i in range(1, a+1):
    if i % 10 in [3, 6, 9]:
        print("X", end=" ")
    else:
        print(i, end=" ")
    
#Q. 7 빛 섞어 색 만들기
r, g, b = map(int, input().split())
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)

print(r*g*b)

#Q. 8 소리 파일 저장용량 계산하기
h, b, c, s = map(int, input().split())
# h = 마이크로 소리 강약 체크 횟수
# b = 한 번 체크한 값을 저장할 때 사용하는 비트수
# c = 좌우 등 소리를 저장할 트랙 개수인 채널 개수
# s = 녹음할 시간(초)
# 필요한 저장공간 = h * b * c * s /8/1024/1024

answer = round(h*b*c*s/8/1024/1024, 1)

print("{} MB".format(answer))

#Q. 9 그림 파일 저장용량 계산하기
w, h, b = map(int, input().split())
# w = 이미지 가로 해상도
# h = 이미지 세로 해상도
# b = 한 픽셀을 저장하기 위한 비트 
# 필요한 저장공간 = h * b * c * s /8/1024/1024

answer = float(w*h*b/8/1024/1024)

print("%.2f MB"%answer)

#Q. 10 거기까지! 이제 그만~
n = int(input())
sum = 0
i = 1

while True:
    sum += i
    i += 1
    if sum >= n:
        print(sum)
        break

#Q. 11 3의 배수는 통과
n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    else:
        print(i, end=" ")

#Q. 12 수 나열하기 (1)
a, d, n = map(int, input().split())
# a (시작값), d (등차의 값), n (몇 번째 수)

answer = a       # (1) for문 사용

for i in range(1, n):
    answer += d
    
print(answer)

answer = a; i = 1 # (2) while문 사용
while i < n:
    answer += d
    i += 1

print(answer)

#Q. 13 수 나열하기 (2)
a, r, n = map(int, input().split())
answer = a       # (1) for문 사용

for i in range(1, n):
    answer *= r
    
print(answer)

#Q. 14 수 나열하기 (3)
a, m, d, n = map(int, input().split())
answer = a       # (1) for문 사용

for i in range(1, n):
    answer = answer * m + d
    
print(answer)

#Q. 15 함께 문제 푸는 날
a, b, c = map(int, input().split()) # 방문 주기 
day = 1

while (day%a) != 0 or (day%b) != 0 or (day%c) != 0:
    day += 1

print(day)
