import re
p = re.compile('[abc]')
m = p.match("a")
print(m)

p = re.compile('[abc]')
m = p.match("before")  # 첫 글자에 b가 있어서 'b'로 매칭
print(m)

p = re.compile('[abc]')
m = p.match('dude')  # 첫 글자에 문자열 클래스에 있는 a, b, c가 모두 없기 때문에 매칭이 되지 않음
print(m)

p = re.compile('[abc]') # 첫 번째 글자에 a, b, c가 없어서 매칭이 되지 않음
m = p.match('dad')    # 두 번째 글자가 문자열 클래스에 있으나 첫번째가 아니기 때문에 매칭이 되지 않음
print(m)

p = re.compile('[def]')  # 첫 번째 클자가 정규식 문자열 클래스에 포함되어 있어서
m = p.match('dad')       # 'd' 로 매칭
print(m)

p = re.compile('d[def]')  # 첫 번째 글자 d는 매칭이 되나 두 번째 글자는 매칭이 되지 않는다.
m = p.match('dad')      # 정규식에 100% 가 매칭이 되어야 반환 되기 때문에 매칭이 되지 않음
print(m)

p = re.compile('d[abc]')  # 문자열을 기준으로는 dad 의 세 번째 글자 d와 매칭이 되지는 않으나
m = p.match('dad')      # 정규식을 기준으로는 d 그리고 [abc] 두 조건이 100% 매치가
print(m)                # 'da'로 되기 때문에 'da' 로 매칭

p = re.compile('d[abc]a')  # 정규식을 기준으로 두 번째 까지는 매칭이 되나, 세 번째가 매칭이 되지 않음
m = p.match('dad')
print(m)

p = re.compile("[abc]d")  # 문자열 ad는 정규식 패턴에 맞게 보일 수 있으나 정규식의 순서와
m = p.match("dad")        # 맞지 않으므로 매칭이 되지 않음
print(m)

p = re.compile("[cd][ab]")  # 첫 글자가 c, d 중에 하나이고 두 번째 글자가 a, b 중에 하나만 정규식이므로
m = p.match("da")           # 'da' 로 매칭
print(m)