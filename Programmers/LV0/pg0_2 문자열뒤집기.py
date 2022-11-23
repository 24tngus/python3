#Q. 문자열 뒤집기 

# 문자열 my_string이 매개변수로 주어집니다. 
# my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = ''
    
    # 1) 슬라이싱 이용 
    answer = [] # 문자열인 경우 answer = ''
    
    answer = my_string[::-1] # 원소 순서를 거꾸로 뒤집기
    
    # 2) for문 이용
    for c in my_string:
        answer = c + answer # 문자열 앞에 다음 문자 추가
        
    # 3) 리스트 reverse() 함수 이용
    ans_list = list(my_string) # 문자열 -> 리스트 
    ans_list.reverse() # 리스트 역순
    
    answer = ''.join(ans_list) # 리스트 -> 문자열
        
    return answer
