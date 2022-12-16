
#Q. 등수 매기기

# 영어 점수와 수학 점수의 평균 점수를 기준으로 학생들의 등수를 매기려고 합니다. 
# 영어 점수와 수학 점수를 담은 2차원 정수 배열 score가 주어질 때, 영어 점수와 수학 점수의 평균을 기준으로 매긴 등수를 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(score):
    answer = []
    num = []
    
    for i in score:
        num.append(sum(i)/len(i))# 평균
    
    # 정렬한 리스트 생성
    num_re = sorted(num, reverse=True)
    
    # num의 순위를 알기 위해 정렬한 리스트에서 num요소 인덱스 반환
    for j in num:
        answer.append(num_re.index(j)+1)
        
    return answer
