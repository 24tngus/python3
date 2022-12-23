T = int(input())

for test_case in range(1, T+1):
    arr = input()
    answer = "YES"
    n = 0
    
    for i in arr:
        if i == "x":
            n += 1
            
        if n >= 8:
            answer = "NO"
    
    print("#{} {}".format(test_case, answer))