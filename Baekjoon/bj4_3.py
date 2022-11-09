#Q. 배열에서 숫자 찾기 

N = int(input()) # 정수의 개수 
arr = list(map(int, input().split()[:N])) # 배열
sel = int(input()) # 찾을 정수 

# count함수 사용
print(arr.count(sel))