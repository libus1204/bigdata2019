import re
# 문자열에 특정 집합 (여기서는 a-z, A-Z, 0-9) 만 들어있는지 확인
text = '2111absdcsac2'
p = re.compile('[^a-zA-Z0-9]$')  # 특수기호가 있을 경우
m = p.search(text)              # 그 문자를 search
m_bool=bool(m)                  # 타입 bool 식으로 변환 (특수기호가 1개라도 있을경우 True)
print(not m_bool)               # 반대로 출력

