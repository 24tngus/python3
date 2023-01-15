---------------------------------------------------------------------------------------------------
T = int(input())

num = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
for test_case in range(1, T+1):
    n = input()
    answer = 0

    word = map(str, input().split())

    for w in word:
        print(num[w])
    
    print("#{} {}".format(test_case, answer))
