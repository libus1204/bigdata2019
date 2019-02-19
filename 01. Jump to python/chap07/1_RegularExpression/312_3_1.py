import re

# str = "\"  # '\' 다음에 escape 코드가 와야 하지만 없으므로 오류 발생
str = "\\"   # str 은 내부적으로 '\\' 저장이 된다. 하지만 문자로서는 '\'의 의미이다.
print(str)   # 출력 결과는 '\'
str = "\\\\" # str 은 내부적으로 '\\\\' 저장이 된다. 하지만 문자로서는 '\\'의 의미이다.
print(str)   # 출력 결과는 '\\'
str = r"\\"  # str 은 내부적으로 '\\\\' 저장이 된다. 하지만 문자로서는 '\\'의 의미이다.
print(str)   # 출력 결과는 '\\'
# str = r"\"   # 현재 버전에서는 'r' raw string 옵션을 사용하고 "\"를 한 개 사용하고
               # '\' 를 한 개 사용하는 것을 허용하지 않는다.
str = "\section"
if str == '\\section':
    print(str)
if str == '\section':
    print(str)