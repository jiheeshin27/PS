# 재귀함수: 하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것

# 자연수의 합 구하기
def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n-1)

# factorial
def fac(n):
    if n <= 1:
        return n
    else: 
        return n * fac(n-1)

# fibonacci
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


# 재귀적 이진탐색
def solution(L, x, l, u):
    if l == u and L[l] != x:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid-1)
    else:
        return solution(L, x, mid+1, u)