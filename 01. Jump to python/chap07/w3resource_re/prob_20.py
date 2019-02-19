import re
# sample text 에서 searched words 가 있는지 검색하고, 패턴이 발생한 문자열 위치 찾기
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = 'fox'
m = re.search(searched_words, sample_text)
# print(m)
print("fox is started at %d and ended at %d" %(m.start(),m.end()))
