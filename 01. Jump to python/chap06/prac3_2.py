import os
import shutil
new_repository = input("변경된 파일 경로를 입력하세요. : ")
now_repository = os.getcwd()
relative_path = os.path.relpath(new_repository, now_repository)
print(relative_path)
print(new_repository[1])
# if new_repository[0] == '.':
#     shutil.copy(relative_path + "\\poll.txt", now_repository)
# elif new_repository[0] == 'D':
#     shutil.copy(new_repository + "/poll.txt", now_repository)