print(abs(-3))  #  절대값

print(all([1,2,3])) # 리스트 자료형에 0이 한개라도 있을 때 False 출력
print(all([1,2,3,0]))

print(any([1,2,3,0]))  # all 의 반대

print(chr(97))  # 아스키 코드값을 입력 받아 그 코드에 해단하는 문자 출력

print(dir([1,2,3]))  # 객체가 자체적으로 갖고 있는 변수나 함수 출력

print(divmod(1.3,0.2))  # a,b 두개 숫자 입력 받고, a와 b를 나눈 몫과 나머지를 튜플 형태로 리턴

for i, name in enumerate(['body', 'foo', 'bar']):  # 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체 리턴
    print(i, name)

print(eval("'hi'+'a'"))  # 실행 가능한 문자열을 입력받아 문자열을 실행한 결과값을 리턴

