T = int(input())

for test_case in range(1, T+1):
    word = input()
    answer = ['']*5

    a = "..#." # 첫번째, 다섯번째 줄
    b = ".#.#" # 두번째, 네번째 줄
    ab_last = "."
    c = "#." # 세번째 줄
    c_last = "#"

    N = len(word)

    answer[0] += a * N + ab_last
    answer[1] += b * N + ab_last
    for i in word:
        answer[2] += c + i + ab_last
    answer[2] += c_last
    answer[3] += b * N + ab_last
    answer[4] += a * N + ab_last

    for line in answer:
        print(line)
