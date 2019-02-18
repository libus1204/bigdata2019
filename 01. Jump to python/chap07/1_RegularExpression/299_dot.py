import re

p = re.compile('.')  # 모든 문자 클래스의 매칭이 된다.
m = p.match('1')     # [] 문자열 클래스가 아닌 일반 문법으로 사용했을 경우
print(m)             # '.' 은 모든 문자를 의미하는 메타 문자로 사용된다.
m = p.match('a')
print(m)
m = p.match('K')
print(m)
m = p.match(' ')
print(m)
m = p.match('*')
print(m)

p = re.compile('...')  # 모든 문자 클래스의 매칭
m = p.match('dad')
print(m)

p = re.compile('...')  # 모든 문자 클래스의 매칭이 된다.
m = p.match('Hi! dad!')
print(m)

p = re.compile('....')  # 모든 문자 클래스의 매칭
m = p.match('pen.')
print(m)

p = re.compile('pen.')  # 모든 문자 클래스의 매칭
m = p.match('pen.')
print(m)
m = p.match('pen!')     # 매칭. '.' 는 모든 문자열 클래스이기 때문
print(m)                # 하지만 '.' 문자 자체를 필터링하는 조건으로는 사용할 수 없다.

p = re.compile('pen[.]')  # '.' 를 메타 문자가 아닌 고유의 문자의미로 정규식을 사용하고 싶다면
m = p.match('pen!')       # '.' 를 문자열 클래스 안에서 사용해야 한다.
print(m)                  # 따라서 pen!는 '.'로 끝나지 않았기 때문에 매칭이 되지 않음