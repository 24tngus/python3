for test_case in range(10):
    T = int(input())
    queue = list(map(int,input().split()))
    i = 1

    while True:
        if i > 5: # i가 5보다 커지면 1로 초기화
            i = 1
            
        end = queue.pop(0) - i # 첫 번째 값빼서 i 만큼 빼기
        i += 1

        if end <= 0:
            queue.append(0)
            break

        queue.append(end)

    print("#{} {} {} {} {} {} {} {} {}". format(test_case + 1, *queue)) # []제외하고 출력
