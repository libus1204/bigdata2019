m, n = input("입력 : ").split(' ')
m = int(m)
n = int(n)
if m == 0:
    print("출력 : %s" %m)
else:
    if m <= n:
        print("출력 : 1")
    else:
        print("출력 : %s" %((m//n)+1))
