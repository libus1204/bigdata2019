import re
# sample text  내 pattern 의 시작과 끝 찾기
sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
m = re.finditer(pattern, sample_text)
for patterns in m:
    print(pattern+" is started at %s and ended at %s." %(patterns.start(), patterns.end()))

