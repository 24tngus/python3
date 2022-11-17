T = int(input())

for test_case in range(1, T+1):
    data = input()

    val_L = 1; val_R = 1 # 트리의 루트 (분자, 분모)

    for i in data:
        if i == 'L':
            val_R = val_L + val_R
        elif i == 'R':
            val_L = val_L + val_R


    print("#{} {} {}". format(test_case, val_L, val_R))