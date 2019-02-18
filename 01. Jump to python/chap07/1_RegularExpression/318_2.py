import re

p = re.compile(r"(\w+)\s+(\d+)[-](\d+)[-](\d+)")
m = p.search("park 010-1234-5678")
print(m)
print(m.group(0))  # 전체 맵핑
print(m.group(1))  # park
print(m.group(2))  # 010
print(m.group(3))  # 1234
print(m.group(4))  # 5678

