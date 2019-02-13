print(hex(234))  # 정수값을 입력 받아 16진수로 변환

a=3
print(id(3))  # 객체를 입력 받아 객체의 고유 주소값(레퍼런스)을 리턴
print(id(a))  # b = a = 3 이므로 셋다 같은 객체를 가리킴
b=a
print(id(b))

class Person: pass

a = Person()
print(isinstance(a,Person))  # a가 Person 의 클래스에 의해서 생성된 인스턴스임을 확인시켜 줌
b = 3
print(isinstance(b,Person))  # b 는 거짓

print(len('python'))  # 입력값 s의 길이 리턴
print(list('python'))  # 자료형 s를 입력 받아 리스트로 만들어 리턴
