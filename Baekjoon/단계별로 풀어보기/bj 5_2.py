# Q. 셀프 넘버

number = list(range(1, 10001))
create = []

for num in number:
    for n in str(num):
        num += int(n)

    if num <= 10000:
        create.append(num)

for create in set(create):
    number.remove(create)

for i in number:
    print(i)