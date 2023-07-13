-------------------------------------------------------------------
T = int(input())

for test_case in range(1, T+1):
    answer = ""
    arr = []

    for _ in range(5):
        arr.append(input())

    max_len = 0
    for r in arr:
        if len(r) > max_len:
            max_len = len(r)

    for i in range(max_len):
        for j in range(5):
            if i < len(arr[j]): # 문자열이 짧은 경우 
                answer += arr[j][i]
    
    print("#{} {}".format(test_case, answer))
