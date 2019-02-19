import re
# sample text 에서 pattern 검색
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
m = re.findall(pattern, sample_text)
for patterns in m:
    print(patterns)
