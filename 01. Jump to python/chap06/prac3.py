def read_content():
    try:
        f = open("poll.txt", 'r',encoding='utf8')
    except FileNotFoundError:
        print('''기존 poll.txt 파일을 찾을 수 없습니다. 아래 중 선택하세요.
1. 종료 2.새로운 파일 생성 3. 변경된 파일 경로 입력: ''', end="")
    else:
        lines = f.readlines()
        print("<현재 누적 응답 현황>")
        for line in lines:
            print(line,end="")
        f.close()
        survey()
def survey():
    why_like_programming = input("프로그래밍이 왜 좋으세요? (종료 입력 시 프로그램 종료) : ")
    if why_like_programming == "종료":
        print("프로그램을 종료합니다.")
        exit()
    whats_your_name = input("이름을 입력해주세요. : ")
    print("설문에 응답해 주셔서 감사합니다.")
    f = open("./poll.txt", 'a', encoding='utf8')
    f.write("[" + whats_your_name + "]" + " ")
    f.write(why_like_programming + "\n")
    f.close()
    read_content()
read_content()
user_input = input()
if user_input == '1':
    print("프로그램을 종료합니다.")
    exit()
elif user_input == '2':
    survey()
elif user_input == '3':
    import os
    import shutil
    new_repository = input("변경된 파일 경로를 입력하세요. : ")
    now_repository = os.getcwd()
    relative_path = os.path.relpath(new_repository, now_repository)
    if new_repository[1] == ':':
        shutil.copy(new_repository + "/poll.txt", now_repository)
    else:
        shutil.copy(relative_path + "\\poll.txt", now_repository)
    survey()