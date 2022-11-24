#Q. 외계어 사전

# 알파벳이 담긴 배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. 
# spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가 dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.

def solution(spell, dic):
    answer = 2
    
    n = len(spell)
    
    for word in dic:
        if len(word) != n:
            continue
            
        cnt = 0
        
        word = list(set(word)) # 중복 제거 
        
        for i in word:
            if i in spell:
                cnt += 1
                
        if cnt == n:
            answer = 1
            
    return answer