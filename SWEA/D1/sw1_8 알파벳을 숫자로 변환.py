T = input() 

for i in T:
    num = ord(i)-64  # ord() : 특정 문자의 아스키코드 값 변환 (A:65)
    print(num, end=' ') # 문자 사이에 공백 출력 

# 딕셔너리 사용

'''
T = str(input())
dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
for i in T:
    print(dic[i], end=' ')
'''
