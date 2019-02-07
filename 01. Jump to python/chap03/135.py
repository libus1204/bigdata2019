for i in range(2,10):
    for j in range(1,10):
        if int(i)*int(j) <10:
            print(" "+int(i)*int(j), end=" ")
        else: print(i*j, end=" ")
    print('')
