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
        g_json_big_data = []
        user_input = input()
        if user_input == '1':
            from collections import OrderedDict
            g_json_big_data2 = OrderedDict()
            g_json_big_data2["address"] = "dummy"
            g_json_big_data2["student_ID"] = "ITT000"
            g_json_big_data2["student_age"] = 0
            g_json_big_data2["student_name"] = "dummy"
            g_json_big_data2["total_course_info"] = {"learning_course_info":
                                                        [{"close_date": "dummy", "course_code": "dummy",
                                                          "course_name": "dummy",
                                                          "open_date": "dummy", "teacher": "dummy"}],
                                                    "num_of_course_learned": "dummy"}
            g_json_big_data.append(g_json_big_data2)
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
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
    print("\n   << Json 기반 주소록 관리 프로그램 >> ")
    print(" 1. 학생 정보입력\n 2. 학생 정보조회\n 3. 학생 정보수정\n 4. 학생 정보삭제\n 5. 프로그램 종료")
    user_input_main_num = input("메뉴 번호를 입력하세요 : ")
    if user_input_main_num == '1':
        menu_1()
    if user_input_main_num == '2':
        menu_2()
    if user_input_main_num == '3':
        menu_3()
    if user_input_main_num == '4':
        menu_4()
    if user_input_main_num == '5':
        menu_5()
def menu_1():
    while True:
        print(" < 학생 정보 입력 > ")
        with open("ITT_Student.json", encoding='UTF8') as json_file:  # 아스키 파일
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            g_json_big_data = json.loads(json_string)
        id = int(g_json_big_data[-1]["student_ID"][3:]) + 1
        student_ID = "ITT"+str(id).zfill(3)
        student_name = input("이름(예 : 홍길동, 엔터 시 종료) : ")
        if not student_name:
            main()
            break
        student_age = input("나이(예 : 29) : ")
        address = input("주소(예 : 대구광역시 동구 아양로 135) : ")
        num_of_course_learned = input("과거 수강 횟수(예 : 1, 없을 경우 '0' 입력) : ")
        course_code = input("강의코드(예 : IB171106 .. 현재 수강중인 강의가 없을 경우 '엔터' 입력) : ")
        if not course_code:
            g_json_big_data.append({"address": address, "student_ID": student_ID, "student_age": int(student_age),
                                    "student_name": student_name, "total_course_info": {"learning_course_info":[],
                                     "num_of_course_learned": int(num_of_course_learned)}})
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
        if g_json_big_data[0]["student_ID"] == "ITT000":
            del g_json_big_data[0]
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
            print("\n입력 하신 정보는 다음과 같습니다.")
            print("학생 ID %s" % student_ID)
            print("이름 : %s" % student_name)
            print("나이 : %s" % student_age)
            print("주소 : %s" % address)
            print("과거 수강 횟수 : %s" % num_of_course_learned)
            menu_1()
            break
        course_name = input("강의명(IoT 빅데이터 실무반) : ")
        teacher = input("강사(예 : 이현구) : ")
        open_date = input("개강일 (예 : 2017-11-06) : ")
        close_date = input("종료일 (예 : 2018-09-05) :  ")
        g_json_big_data.append({"address": address, "student_ID": student_ID, "student_age": int(student_age),
                                "student_name":student_name, "total_course_info":{"learning_course_info":
                                [{"close_date": close_date, "course_code": course_code, "course_name": course_name,
                                "open_date": open_date, "teacher":teacher}],"num_of_course_learned": int(num_of_course_learned)}})
        if g_json_big_data[0]["student_ID"] == "ITT000":
            del g_json_big_data[0]
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
        print("\n입력 하신 정보는 다음과 같습니다.")
        print("학생 ID %s" % student_ID)
        print("이름 : %s" % student_name)
        print("나이 : %s" % student_age)
        print("주소 : %s" % address)
        print("- 수강정보\n  > 과거 수강 횟수 : %s" % num_of_course_learned)
        print("  > 현재 수강 과목\n    + 강의 코드 : %s" % course_code)
        print("    + 강의명 : %s" % course_name)
        print("    + 강사 : %s" % teacher)
        print("    + 개강일 : %s" % open_date)
        print("    + 종료일 : %s" % close_date)
def menu_2():
    print("\n < 학생 정보 조회 >")
    print("1. 전체 학생 조회\n2. 학생 정보 검색\n3. 상위메뉴")
    user_menu_2_input = input("번호를 입력하세요 : ")
    if user_menu_2_input == '1':
        menu_2_1()
    elif user_menu_2_input == '2':
        menu_2_2()
    elif user_menu_2_input == '3':
        main()
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
        if not g_json_big_data[student]["total_course_info"]["learning_course_info"]:
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
    menu_2()
def menu_2_2():
    students_match = []
    with open("ITT_Student.json", encoding='UTF8') as json_file:  # 아스키 파일
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)
    students_count = len(g_json_big_data)
    print("1. ID\n2. 이름\n3. 나이\n4. 주소\n5. 과거 수강 횟수\n6. 현재 강의를 수강하고 있는 학생\n7. 현재 수강 과목의 "
          "강의명\n8. 현재 수강 과목의 강사명\n9. 이전 메뉴")
    user_menu_2_2_match = input("번호를 입력하세요 : ")
    if user_menu_2_2_match == '9':
        main()
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
            if g_json_big_data[student]["student_age"] == int(user_menu_2_2_search):
                students_match.append(student)
    if user_menu_2_2_match == '4':
        for student in range(students_count):
            if user_menu_2_2_search in g_json_big_data[student]["address"]:
                students_match.append(student)
    if user_menu_2_2_match == '5':
        for student in range(students_count):
            if g_json_big_data[student]["total_course_info"]["num_of_course_learned"] == int(user_menu_2_2_search):
                students_match.append(student)
    if user_menu_2_2_match == '7':
        for student in range(students_count):
            for i in range(len(g_json_big_data[student]["total_course_info"]["learning_course_info"])):
                if user_menu_2_2_search in g_json_big_data[student]["total_course_info"]["learning_course_info"][i]["course_name"] :
                    students_match.append(student)
    if user_menu_2_2_match == '8':
        for student in range(students_count):
            for i in range(len(g_json_big_data[student]["total_course_info"]["learning_course_info"])):
                if user_menu_2_2_search in g_json_big_data[student]["total_course_info"]["learning_course_info"][i]["teacher"]:
                   students_match.append(student)
    if not len(students_match):
        print("검색 결과가 없습니다")
    elif len(students_match) == 1:
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
    elif len(students_match) > 1:
        print("복수 개의 결과가 검색되었습니다.\n  ----- 요약 결과 ----- ")
        for i in students_match:
            print("이름 : %s [%s]" %(g_json_big_data[i]["student_name"], g_json_big_data[i]["student_ID"]))
    menu_2()
def menu_3():
    with open("ITT_Student.json", encoding='UTF8') as json_file:  # 아스키 파일
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)
    user_want_modify = input("수정할 학생의 ID 번호를 입력하세요 : ")
    students_count = len(g_json_big_data)
    for student in range(students_count):
        if g_json_big_data[student]["student_ID"] == user_want_modify:
            student_modify = student
    print("----------------------------------------------------------")
    print("1. ID : %s" % g_json_big_data[student_modify]["student_ID"])
    print("2. 이름 : %s" % g_json_big_data[student_modify]["student_name"])
    print("3. 나이 : %s" % g_json_big_data[student_modify]["student_age"])
    print("4. 주소 : %s" % g_json_big_data[student_modify]["address"])
    print("5. 과거 수강 횟수 : %s" % g_json_big_data[student_modify]["total_course_info"]["num_of_course_learned"])
    if not g_json_big_data[student_modify]["total_course_info"]["learning_course_info"]:
        print("6. 현재 수강 과목이 없습니다.")
        user_want_modify_num = input("수정할 번호를 입력하세요(과목을 추가하시려면 '6', 메뉴로 돌아가려면 '엔터'입력) : ")
        if user_want_modify_num == '6':
            while True:
                add_course_code = input("추가하실 과목의 코드를 입력하세요(메뉴로 돌아가려면 '엔터' 입력) : ")
                if not add_course_code:
                    print("1. ID : %s" % g_json_big_data[student_modify]["student_ID"])
                    print("2. 이름 : %s" % g_json_big_data[student_modify]["student_name"])
                    print("3. 나이 : %s" % g_json_big_data[student_modify]["student_age"])
                    print("4. 주소 : %s" % g_json_big_data[student_modify]["address"])
                    print("5. 과거 수강 횟수 : %s" % g_json_big_data[student_modify]["total_course_info"][
                        "num_of_course_learned"])
                    course_count = 6
                    print("- 현재 수강 과목")
                    for i in range(len(g_json_big_data[student_modify]["total_course_info"]["learning_course_info"])):
                        print("%s. 강의 코드 : %s" % (course_count, g_json_big_data[student_modify]["total_course_info"]
                        ["learning_course_info"][i]["course_code"]))
                        print("%s. 강의명 : %s" % (course_count + 1, g_json_big_data[student_modify]["total_course_info"]
                        ["learning_course_info"][i]["course_name"]))
                        print("%s. 강사 : %s" % (course_count + 2, g_json_big_data[student_modify]["total_course_info"]
                        ["learning_course_info"][i]["teacher"]))
                        print("%s. 개강일 : %s" % (course_count + 3, g_json_big_data[student_modify]["total_course_info"]
                        ["learning_course_info"][i]["open_date"]))
                        print("%s. 종료일 : %s" % (course_count + 4, g_json_big_data[student_modify]["total_course_info"]
                        ["learning_course_info"][i]["close_date"]))
                        course_count += 5
                    main()
                    break
                add_course_name = input("추가하실 과목의 과목명을 입력하세요 : ")
                add_course_teacher = input("추가하실 과목의 강사명을 입력하세요 : ")
                add_course_open = input("추가하실 과목의 개강일을 입력하세요 : ")
                add_course_close = input("추가하실 과목의 종료일을 입력하세요 : ")
                g_json_big_data[student_modify]["total_course_info"]["learning_course_info"].append({"close_date":
                add_course_close,"course_code": add_course_code, "course_name": add_course_name,"open_date":
                add_course_open, "teacher": add_course_teacher})
                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
            print("1. ID : %s" % g_json_big_data[student_modify]["student_ID"])
            print("2. 이름 : %s" % g_json_big_data[student_modify]["student_name"])
            print("3. 나이 : %s" % g_json_big_data[student_modify]["student_age"])
            print("4. 주소 : %s" % g_json_big_data[student_modify]["address"])
            print("5. 과거 수강 횟수 : %s" % g_json_big_data[student_modify]["total_course_info"]["num_of_course_learned"])
            course_count = 6
            print("- 현재 수강 과목")
            for i in range(len(g_json_big_data[student_modify]["total_course_info"]["learning_course_info"])):
                print("%s. 강의 코드 : %s" % (course_count, g_json_big_data[student_modify]["total_course_info"]
                ["learning_course_info"][i]["course_code"]))
                print("%s. 강의명 : %s" % (course_count + 1, g_json_big_data[student_modify]["total_course_info"]
                ["learning_course_info"][i]["course_name"]))
                print("%s. 강사 : %s" % (course_count + 2, g_json_big_data[student_modify]["total_course_info"]
                ["learning_course_info"][i]["teacher"]))
                print("%s. 개강일 : %s" % (course_count + 3, g_json_big_data[student_modify]["total_course_info"]
                ["learning_course_info"][i]["open_date"]))
                print("%s. 종료일 : %s" % (course_count + 4, g_json_big_data[student_modify]["total_course_info"]
                ["learning_course_info"][i]["close_date"]))
                course_count += 5
        elif not user_want_modify_num:
            menu_3()
        user_want_modify_cont = input("수정할 내용을 입력하세요 : ")
        if user_want_modify_num == '1':
            g_json_big_data[student_modify]["student_ID"] = user_want_modify_cont
        elif user_want_modify_num == '2':
            g_json_big_data[student_modify]["student_name"] = user_want_modify_cont
        elif user_want_modify_num == '3':
            g_json_big_data[student_modify]["student_age"] = int(user_want_modify_cont)
        elif user_want_modify_num == '4':
            g_json_big_data[student_modify]["address"] = user_want_modify_cont
        elif user_want_modify_num == '5':
            g_json_big_data[student_modify]["total_course_info"]["num_of_course_learned"] = user_want_modify_cont

        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
    else:
        course_count = 6
        print("- 현재 수강 과목")
        for i in range(len(g_json_big_data[student_modify]["total_course_info"]["learning_course_info"])):
            print("%s. 강의 코드 : %s" % (course_count, g_json_big_data[student_modify]["total_course_info"]
                                        ["learning_course_info"][i]["course_code"]))
            print("%s. 강의명 : %s" % (course_count+1, g_json_big_data[student_modify]["total_course_info"]
                                        ["learning_course_info"][i]["course_name"]))
            print("%s. 강사 : %s" % (course_count+2, g_json_big_data[student_modify]["total_course_info"]
                                        ["learning_course_info"][i]["teacher"]))
            print("%s. 개강일 : %s" % (course_count+3 ,g_json_big_data[student_modify]["total_course_info"]
                                        ["learning_course_info"][i]["open_date"]))
            print("%s. 종료일 : %s" % (course_count+4, g_json_big_data[student_modify]["total_course_info"]
                                        ["learning_course_info"][i]["close_date"]))
            course_count += 5
    user_want_modify_num = input("수정할 번호를 입력하세요 : ")
    user_want_modify_cont = input("수정할 내용을 임력하세요 : ")
    if user_want_modify_num == '1':
        g_json_big_data[student_modify]["student_ID"] = user_want_modify_cont
    if user_want_modify_num == '2':
        g_json_big_data[student_modify]["student_name"] = user_want_modify_cont
    if user_want_modify_num == '3':
        g_json_big_data[student_modify]["student_age"] = int(user_want_modify_cont)
    if user_want_modify_num == '4':
        g_json_big_data[student_modify]["address"] = user_want_modify_cont
    if user_want_modify_num == '5':
        g_json_big_data[student_modify]["total_course_info"]["num_of_course_learned"] = int(user_want_modify_cont)
    if int(user_want_modify_num) >= 6:
        summary_course = g_json_big_data[student_modify]["total_course_info"]["learning_course_info"]
        cal = (int(user_want_modify_num) - 6) // 5
        if int(user_want_modify_num) % 5 == 1:
            summary_course[cal]["course_code"] = user_want_modify_cont
        elif int(user_want_modify_num) % 5 == 2:
            summary_course[cal]["course_name"] = user_want_modify_cont
        elif int(user_want_modify_num) % 5 == 3:
            summary_course[cal]["teacher"] = user_want_modify_cont
        elif int(user_want_modify_num) % 5 == 4:
            summary_course[cal]["open_date"] = user_want_modify_cont
        elif int(user_want_modify_num) % 5 == 0:
            summary_course[cal]["close_date"] = user_want_modify_cont
    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
    print("학생 ID : %s" % g_json_big_data[student_modify]["student_ID"])
    print("이름 : %s" % g_json_big_data[student_modify]["student_name"])
    print("나이 : %s" % g_json_big_data[student_modify]["student_age"])
    print("주소 : %s" % g_json_big_data[student_modify]["address"])
    print("- 수강정보")
    if not g_json_big_data[student_modify]["total_course_info"]["num_of_course_learned"]:
        print("과거에 수강한 과목이 없습니다.")
        print("  > 현재 수강 과목")
        for i in range(len(g_json_big_data[student_modify]["total_course_info"]["learning_course_info"])):
            print("    + 강의 코드 : %s" %
                  g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i]["course_code"])
            print("    + 강의명 : %s" % g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i][
                "course_name"])
            print("    + 강사 : %s" % g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i][
                "teacher"])
            print("    + 개강일 : %s" % g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i][
                "open_date"])
            print("    + 종료일 : %s" % g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i][
                "close_date"])
    print("- 과거 수강 횟수 : %s" % g_json_big_data[student_modify]["total_course_info"]["num_of_course_learned"])
    if not g_json_big_data[student_modify]["total_course_info"]["learning_course_info"]:
        print("  > 현재 수강 과목하는 과목이 없습니다")
    else:
        print("  > 현재 수강 과목")
        for i in range(len(g_json_big_data[student_modify]["total_course_info"]["learning_course_info"])):
            print("    + 강의 코드 : %s" %
                  g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i]["course_code"])
            print("    + 강의명 : %s" % g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i][
                "course_name"])
            print("    + 강사 : %s" % g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i][
                "teacher"])
            print("    + 개강일 : %s" % g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i][
                "open_date"])
            print("    + 종료일 : %s" % g_json_big_data[student_modify]["total_course_info"]["learning_course_info"][i][
                "close_date"])
    main()
def menu_4():
    with open("ITT_Student.json", encoding='UTF8') as json_file:  # 아스키 파일
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        g_json_big_data = json.loads(json_string)
    user_delete = input("삭제하실 학생 ID를 입력하세요 : ")
    students_count = len(g_json_big_data)
    for student in range(students_count):
        if g_json_big_data[student]["student_ID"] == user_delete:
            student_delete = student
    print("삭제 유형을 선택하세요.\n1. 전체 삭제\n2. 현재 수강 중인 특정 과목정보 삭제\n3. 이전 메뉴")
    user_delete_cate = input("메뉴 번호를 선택하세요 : ")
    if user_delete_cate == '1':
        del g_json_big_data[student_delete]
        with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
            readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
            outfile.write(readable_result)
    elif user_delete_cate == '3':
        main()
    elif user_delete_cate == '2':
        course_len = len(g_json_big_data[student_delete]["total_course_info"]["learning_course_info"])
        if course_len == 0:
            print("현재 수강중인 강의가 없습니다.\n메뉴로 돌아갑니다.")
            main()
        elif course_len == 1:
            del g_json_big_data[student_delete]["total_course_info"]["learning_course_info"][0]["close_date"]
            del g_json_big_data[student_delete]["total_course_info"]["learning_course_info"][0]["course_code"]
            del g_json_big_data[student_delete]["total_course_info"]["learning_course_info"][0]["course_name"]
            del g_json_big_data[student_delete]["total_course_info"]["learning_course_info"][0]["open_date"]
            del g_json_big_data[student_delete]["total_course_info"]["learning_course_info"][0]["teacher"]
        elif course_len >= 2:
            print("삭제할 강의를 선택해 주세요.")
            course_len_count = 1
            for i in range(course_len):
                print("%s. %s" % (course_len_count, g_json_big_data[student_delete]["total_course_info"]
                                  ["learning_course_info"][i]["course_name"]))
                course_len_count += 1
            user_course_del_select = int(input("번호를 선택해주세요 : "))
            del g_json_big_data[student_delete]["total_course_info"]["learning_course_info"][user_course_del_select-1]
    with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
        readable_result = json.dumps(g_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(readable_result)
    print("삭제 되었습니다. 메뉴로 돌아갑니다.")
    main()
def menu_5():
    print("프로그램을 종료합니다.")
    exit()

read_content()


