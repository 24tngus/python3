#Q. 더하기 사이클

N = int(input())

len=0
new = -1

while N!=new:
    if(new == -1):
        new = N
    new = new%10*10+(new//10+new%10)%10  # 조건 만족하는 식 생성 
    len += 1    # 길이 측정 

print(len)
