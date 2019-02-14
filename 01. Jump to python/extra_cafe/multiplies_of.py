X, Y, Z =input("공배수를 구할 두 숫자와 범위를 차례대로 입력하세요.(공백으로 구분), 0 입력시 종료 : ").split(' ')
if int(X)==0 and int(Y)==0 and int(Z)==0:
    print("프로그램을 종료합니다.")
    exit()
else:
    for i in range(1,int(Z)):
        if i%int(X) == 0 and i%int(Y) ==0:
            print(i, end=" ")

