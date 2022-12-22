T = int(input())

for test_case in range(1, T+1):
    word = input()
    answer = 0 # 공의 개수 
    # (, ), () 개수 구하기 (반쪽일 경우 "(|"로 찾기))

    for i in range(len(word)):
        if word[i:i+2] == "()":
            answer += 1
        elif word[i:i+2] == "(|" or word[i:i+2] == "|)":
            answer += 1
          
    print("#{} {}". format(test_case, answer))