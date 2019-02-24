import json

def read_content():
    print("파일을 불러오는 중 입니다 ... ")
    try:
        with open("ITT_Student.json", encoding='UTF8') as json_file:  # 아스키 파일
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            g_json_big_data = json.loads(json_string)
    except FileNotFoundError:
        print('''\n파일을 찾을 수 없습니다. 아래 번호를 선택하세요.
1. 새로운 파일 생성하기\n2. 경로지정하기
번호를 입력하세요 : ''', end=" ")
        user_input = input()
        if user_input == '1':
            main()
        elif user_input == '2':
            import os
            import shutil
            new_repository = input("변경된 파일 경로를 입력하세요. : ")
            now_repository = os.getcwd()
            relative_path = os.path.relpath(new_repository, now_repository)
            if (new_repository[0] == 'C' or new_repository[0] == 'D') and new_repository[1] == ':':
                shutil.copy(new_repository + "/ITT_Student.json", now_repository)
            else:
                shutil.copy(relative_path + "\\ITT_Student.json", now_repository)
            main()
    else:
        main()
def main():
    print("   << json기반 주소록 관리 프로그램 >> ")
    print(" 1. 학생 정보입력\n 2. 학생 정보조회\n 3. 학생 정보수정\n 4. 학생 정보삭제\n 5. 프로그램 종료")
    user_input_main_num = input("메뉴 번호를 입력하세요 : ")
    if user_input_main_num == '1':
        menu_1()
    if user_input_main_num == '2':
        menu_2()
    # if user_input_main_num == '3':
    #     menu_3()
def menu_1():
    while True:
        print(" < 학생 정보 입력 > ")
        with open("ITT_Student.json", encoding='UTF8') as json_file:  # 아스키 파일
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            g_json_big_data = json.loads(json_string)
        id = int(g_json_big_data[-1]["student_ID"][3:]) + 1
        student_ID = "ITT"+str(id).zfill(3)
        student_name = input("이름을 입력하세요(엔터 시 종료) : ")
        if not student_name:
            main()
            break
        student_age = input("나이를 입력하세요 : ")
        address = input("주소를 입력하세요 : ")
        num_of_course_learned = input("과거 수강 횟수를 입력하세요.(없을 경우 '0' 입력) : ")
        course_code = input("현재 수강하고 있는 강의의 코드를 입력하세요 : ")
        course_name = input("현재 수강하고 있는 강의명을 입력하세요 : ")
        teacher = input("현재 수강하고 있는 강의의 강사명을 입력하세요 : ")
        open_date = input("현재 수강하고 있는 강의의 시작일을 입력하세요 : ")
        close_date = input("현재 수강하고 있는 강의의 종료일을 입력하세요 : ")
        g_json_big_data.append({"address": address, "student_ID": student_ID, "student_age": student_age,
                                "student_name":student_name, "total_course_info":{"learning_course_info":
                                [{"close_date": close_date, "course_code": course_code, "course_name": course_name,
                                "open_date": open_date, "teacher":teacher}],"num_of_course_learned": num_of_course_learned}})
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
        print("\n입력 하신 정보는 다음과 같습니다.")
        print("학생 ID %s" %student_ID)
        print("이름 : %s" %student_name)
        print("나이 : %s" %student_age)
        print("주소 : %s" %address)
        print("- 수강정보\n  > 과거 수강 횟수 : %s" %num_of_course_learned)
        print("  > 현재 수강 과목\n    + 강의 코드 : %s" %course_code)
        print("    + 강의명 : %s" %course_name)
        print("    + 강사 : %s" %teacher)
        print("    + 개강일 : %s" %open_date)
        print("    + 종료일 : %s" %close_date)
def menu_2():
    print(" < 학생 정보 조회 >")
    print("1. 전체 학생 조회\n2. 학생 정보 검색")
    user_menu_2_input = input("번호를 입력하세요 : ")
    if user_menu_2_input == '1':
        menu_2_1()
    elif user_menu_2_input == '2':
        menu_2_2()
def menu_2_1():
    with open("ITT_Student.json", encoding='UTF8') as json_file:  # 아스키 파일
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)
    print("")
    students_count = len(g_json_big_data)
    for student in range(students_count):
        print("")
        print("학생 ID : %s" % g_json_big_data[student]["student_ID"])
        print("이름 : %s" % g_json_big_data[student]["student_name"])
        print("나이 : %s" % g_json_big_data[student]["student_age"])
        print("주소 : %s" % g_json_big_data[student]["address"])
        print("- 수강정보")
        if not g_json_big_data[student]["total_course_info"]["num_of_course_learned"]:
            print("과거에 수강한 과목이 없습니다.")
            print("  > 현재 수강 과목")
            for i in range(len(g_json_big_data[student]["total_course_info"]["learning_course_info"])):
                print("    + 강의 코드 : %s" %
                      g_json_big_data[student]["total_course_info"]["learning_course_info"][i]["course_code"])
                print("    + 강의명 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                    "course_name"])
                print("    + 강사 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                    "teacher"])
                print("    + 개강일 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                    "open_date"])
                print("    + 종료일 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                    "close_date"])
        print("- 과거 수강 횟수 : %s" % g_json_big_data[student]["total_course_info"]["num_of_course_learned"])
        if g_json_big_data[student]["total_course_info"]["learning_course_info"][0] == {}:
            print("  > 현재 수강 과목하는 과목이 없습니다")
        else:
            print("  > 현재 수강 과목")
            for i in range(len(g_json_big_data[student]["total_course_info"]["learning_course_info"])):
                print("    + 강의 코드 : %s" %
                      g_json_big_data[student]["total_course_info"]["learning_course_info"][i]["course_code"])
                print("    + 강의명 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                    "course_name"])
                print("    + 강사 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                    "teacher"])
                print("    + 개강일 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                    "open_date"])
                print("    + 종료일 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                    "close_date"])
def menu_2_2():
    students_match = []
    with open("ITT_Student.json", encoding='UTF8') as json_file:  # 아스키 파일
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)
    students_count = len(g_json_big_data)
    print("검색할 내용의 번호를 입력하세요 : ")
    print("1. ID\n2. 이름\n3. 나이\n4. 주소\n5. 과거 수강 횟수\n6. 현재 강의를 수강하고 있는 학생\n7. 현재 수강 과목의 "
          "강의명\n8. 현재 수강 과목의 강사명")
    user_menu_2_2_match = input("번호를 입력하세요 : ")
    if user_menu_2_2_match == '6':
        for student in range(students_count):
            if g_json_big_data[student]["total_course_info"]["learning_course_info"][0]:
                print("이름 : %s [%s]" % (g_json_big_data[student]["student_name"], g_json_big_data[student]["student_ID"]))
        menu_2()
    user_menu_2_2_search = input("검색어를 입력하세요 : ")
    if user_menu_2_2_match == '1':
        for student in range(students_count):
            if g_json_big_data[student]["student_ID"] == user_menu_2_2_search:
                students_match.append(student)
    if user_menu_2_2_match == '2':
        for student in range(students_count):
            if user_menu_2_2_search in g_json_big_data[student]["student_name"]:
                students_match.append(student)
    if user_menu_2_2_match == '3':
        for student in range(students_count):
            if g_json_big_data[student]["student_age"] == user_menu_2_2_search:
                students_match.append(student)
    if user_menu_2_2_match == '4':
        for student in range(students_count):
            if user_menu_2_2_search in g_json_big_data[student]["address"]:
                students_match.append(student)
    if user_menu_2_2_match == '5':
        for student in range(students_count):
            if g_json_big_data[student]["total_course_info"]["num_of_course_learned"] == user_menu_2_2_search:
                students_match.append(student)
    if user_menu_2_2_match == '7':
        for student in range(students_count):
            if user_menu_2_2_search in g_json_big_data[student]["total_course_info"]["learning_course_info"][0]["course_name"] :
                students_match.append(student)
    if user_menu_2_2_match == '8':
        for student in range(students_count):
            if user_menu_2_2_search in g_json_big_data[student]["total_course_info"]["learning_course_info"][0]["teacher"]:
                students_match.append(student)
    if not len(students_match):
        print("검색 결과가 없습니다")
    if len(students_match) == 1:
        student = students_match[0]
        print("학생 ID : %s" % g_json_big_data[student]["student_ID"])
        print("이름 : %s" % g_json_big_data[student]["student_name"])
        print("나이 : %s" % g_json_big_data[student]["student_age"])
        print("주소 : %s" % g_json_big_data[student]["address"])
        print("- 수강정보\n  > 과거 수강 횟수 : %s" % g_json_big_data[student]["total_course_info"]["num_of_course_learned"])
        if g_json_big_data[student]["total_course_info"]["learning_course_info"][0] == {}:
            print("  > 현재 수강 과목하는 과목이 없습니다")
        else:
            for i in range(len(g_json_big_data[student]["total_course_info"]["learning_course_info"])):
                print("  > 현재 수강 과목\n    + 강의 코드 : %s" %
                  g_json_big_data[student]["total_course_info"]["learning_course_info"][i]["course_code"])
                print("    + 강의명 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                "course_name"])
                print("    + 강사 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                "teacher"])
                print("    + 개강일 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                "open_date"])
                print("    + 종료일 : %s" % g_json_big_data[student]["total_course_info"]["learning_course_info"][i][
                "close_date"])
    if len(students_match) > 1:
        for i in range(len(students_match)):
            print("이름 : %s [%s]" %(g_json_big_data[i]["student_name"], g_json_big_data[i]["student_ID"]))

    menu_2()
# def menu_3():


# while True:
read_content()


