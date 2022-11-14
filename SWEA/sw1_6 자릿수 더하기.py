T = int(input())
answer = 0

str_T = str(T)
for i in str_T:
    answer += int(i)

print(answer)