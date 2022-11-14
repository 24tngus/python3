#Q. 암호해독

def solution(cipher, code):
    answer = ''
    
    # 문자열에서 code배수번째 문자 추출 
    for i in range(code,len(cipher)+1):
        if i%code == 0:
            answer += cipher[i-1]
            
    return answer