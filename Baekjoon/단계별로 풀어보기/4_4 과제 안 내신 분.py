# Q. 과제 안 내신 분..?

arr = [i for i in range(1, 31)]

for _ in range(28):
    N = int(input())
    arr.remove(N)


print(min(arr))
print(max(arr))
