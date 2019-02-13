print(max([1,2,3]))  # 자료형을 입력 받아 최대값 리턴
print(min('PyThOn'))  # 자료형을 입력 받아 최소값 리턴

print(oct(34))  # 정수 형태 숫자를 8진수 문자열로 바꿔 리턴

print(ord('a'))  # 문자의 아스키 코드값을 리턴  # 중요

print(pow(3,3))  # x에 y 제곱한 값 리턴

print(list(range(1,10,2)))  # 1부터 9까지, 숫자 사이 거리는 2 리스트 리턴

print(sorted(['a','d','c']))  # 입력값을 정렬한 후 그 결과를 리스트로 리턴
print(sorted('zero'))

a = [3,1,2]
result = a.sort()
print(result)  # sort 함수는 리턴값이 없기 때문에 result 변수에 저장되는 값이 없다. None 출력