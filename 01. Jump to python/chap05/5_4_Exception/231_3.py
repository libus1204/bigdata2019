denominator = int(input("분수를 입력하세요.: " ))
try:
    f=open("foo.txt", 'r')
    result = 4/denominator
except Exception as e:
    print(e)
finally:
    print("Finally 블록 수행")
    f.close()

# except, finally 모두 수행