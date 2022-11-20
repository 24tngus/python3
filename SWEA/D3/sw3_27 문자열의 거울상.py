T = int(input())

for test_case in range(1, T+1):
    string = input()
    string = string[::-1] # 역순으로 뒤집기

    temp = []

    for i in range(len(string)):
        if string[i] == 'q':
            temp.append('p')
        elif string[i] == 'p':
            temp.append('q')
        elif string[i] == 'd':
            temp.append('b')
        elif string[i] == 'b':
            temp.append('d')

    print("#{} {}". format(test_case, ''.join(temp)))