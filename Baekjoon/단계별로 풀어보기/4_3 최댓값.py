# Q. 최댓값

arr = []

for _ in range(9):
    arr.append(int(input()))

print(max(arr))
print(arr.index(max(arr))+1)
