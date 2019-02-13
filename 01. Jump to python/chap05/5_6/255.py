import os
f=os.popen("dir")
print(f.read())

# f=os.mkdir('tt.txt')  # 디렉 생성
# f = os.rmdir('tt.txt')  # 디렉 삭제
# f = os.unlink('test.txt')  # 파일 삭제
f = os.rename('새폴더', '새폴더2')
