PI = 3.141592
class Math:
    def solv(self,r):
        return PI * (r**2)
    def sum(self,a,b):
        return a+b

if __name__ == "__main__": # 여기서 바로 확인 하려고 사용
    print(PI) # 3.141592
    a = Math() # Math 클래스 생성
    print(a.solv(2)) # 3.141592 * (2^2)
    print(a.sum(PI,4.4)) # 3.141592 + 4.4