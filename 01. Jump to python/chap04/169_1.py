def fib(n):
    if n==0: return 0
    if n==1: return 1
    return fib(n-2)+fib(n-1)

n=int(input("피보나치 수열 입력: "))
for n in range(0,n+1):
    print(fib(n), end=' ')