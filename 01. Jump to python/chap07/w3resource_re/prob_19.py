import re
# sample text 에서 searched words 가 있는지 없는지 확인
sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']
for check in searched_words:
    print(check+" is", end=" ")
    if re.search(check, sample_text):
        print("in sample text.")
    else: print("not in sample text.")