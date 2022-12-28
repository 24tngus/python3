# 버블 정렬 슈도코드
'''
def BubbleSort(a):
    for i in range(len(a)-1),0,-1):
        for j in range(0,i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
'''

# 카운팅 정렬 슈도코드
'''
def CountingSort(A, B, k):
    # A[1..n] = 입력 리스트 사용된 숫자 (1~k)
    # B[1..n] = 정렬된 리스트
    # C[1..n] = 카운트 리스트 

    C = [0] * k

    for i in range(0, len(B)):
        C[A[i]] += 1  # 각 숫자의 자리값에 +1

    for i in range(1, len(C)):
        C[i] += C[i-1] # 정렬시 입력할 위치 계산

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0] * len(a)

CountingSort(a, b, 5)
print(b)
'''