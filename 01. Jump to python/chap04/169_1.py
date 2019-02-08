def fib(n):
    if n==0: return 0
    if n==1: return 1
    return fib(n-2)+fib(n-1)

print(fib(6)) # 피보나치 수열 6일때 값 출력