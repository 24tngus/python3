def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def solution(n):
    answer = fac(n)

    return answer