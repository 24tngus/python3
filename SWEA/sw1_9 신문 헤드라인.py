T = input()
answer = ''

for i in T:
    if i.islower():
        answer += i.upper()
    else:
        answer += i

print(answer)