try:
    f=open("foo.txt", 'r')
except FileNotFoundError as e:
    print(str(e))
# else:
#     data = f.read()
#     f.close()
data = f.read()
f.close()
# 주석이나 밑코드 나 같음