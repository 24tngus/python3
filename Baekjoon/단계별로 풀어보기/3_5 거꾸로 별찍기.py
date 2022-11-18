#Q. 거꾸로 별찍기

N = int(input())

for i in range(1,N+1):
    print(' '*(N-i)+"*"*i) # ,로 연결하면 공백 생겨 + 사용해 문자열로 만듦
