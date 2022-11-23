#Q. 영어가 싫어요

# 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 
#  문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

def solution(numbers):
    answer = []
    
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for index, x in enumerate(num):
        numbers = numbers.replace(x, str(index))
        
    answer = int(numbers)
    
    return answer