#Q. 직각삼각형 출력하기

n = int(input())
tree = ''

for i in range(1,n+1):
    for j in range(1,i+1):
        tree += '*'
    tree += '\n'
print(tree)

# 출력 예시 (ex. 입력 3)
# *
# **
# ***