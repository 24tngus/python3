T = 10

for test_case in range(1, T+1):
    N = int(input()) # 원본 암호문의 길이
    crypto = list(map(int, input().split())) # 원본 암호문
    M = int(input()) # 명령어의 개수
    com = list(input().split()) # 명령어 

    arr = []
    for i in range(len(com)):
        if com[i] in ["I", "D", "A"]:
            if i != 0:
                arr.append(tmp)
            tmp = [com[i]]
        elif i == len(com)-1:
            tmp.append(com[i])
            arr.append(tmp)
        else:
            tmp.append(com[i])

    for i in range(M):
        if arr[i][0] == "I":
            x = int(arr[i][1])
            y = int(arr[i][2])
            s = arr[i][3:]
            for j in range(y):
                crypto.insert(x+j, int(s[j]))

        elif arr[i][0] == "D":
            x = int(arr[i][1])
            y = int(arr[i][2])
            for j in range(y):
                del(crypto[x])
        
        elif arr[i][0] == "A":
            y = int(arr[i][1])
            s = arr[i][2:]
            for j in range(y):
                crypto.append(int(s[j]))      
                     
    print("#{} {} {} {} {} {} {} {} {} {} {}". format(test_case, *crypto))