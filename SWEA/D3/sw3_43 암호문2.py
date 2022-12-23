T = 10

for test_case in range(1, T+1):
    N = int(input()) # 원본 암호문 길이
    arr = list(map(str, input().split())) # 원본 암호문
    N2 = int(input()) # 명령어 개수 
    arr2 = list(map(str, input().split())) # 명령어 

    for i in range(len(arr2)):
        if arr2[i] == "I":
            x = int(arr2[i+1])
            y = int(arr2[i+2])
            s = arr2[i+3:i+y+3]
            for j in range(len(s)):
                arr.insert(x+j, s[j])
        elif arr2[i] == "D":
            x = int(arr2[i+1])
            y = int(arr2[i+2])
            del arr[x: x+y]
            print(arr)
    
    answer = " ".join(arr[:10])

    print("#{} {}".format(test_case, answer))