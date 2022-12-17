# Q. 옹알이
# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요

def solution(babbling):
    answer = 0
    babble = ["aya", "ye", "woo", "ma"] # 문자열 리스트
    for i in babbling:
        for j in babble:
            if j+j in i: # 중복 문자열 제거 
                break
            else:
                i = i.replace(j,"").strip()
                
        if i:
            print("i의 값은 {}",i)
            continue
        else:
            answer += 1
            
    return answer
