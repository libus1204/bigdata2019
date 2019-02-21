from xml.etree.ElementTree import parse
tree = parse("students_info.xml")
raw_info = tree.getroot()
stu_male_total = 0
stu_fem_total = 0
while True:
    print("학생정보 데이터 분석 시작")
    print("1. 요약정보")
    print("2. 전체 데이터 조회")
    print("3. 종료")
    menu_choice = input("메뉴 입력 : ")
    if menu_choice == "1":
        stu_total = str(len(raw_info.findall("student")))
        print("*전체학생수: "+stu_total)
        print("성별")
        stu_list = raw_info.getiterator("student")
        for stu in stu_list:
            if stu.get("sex") == "남":
                stu_male_total +=1
            elif stu.get("sex") == "여":
                stu_fem_total +=1
        stu_male_per = stu_male_total/(stu_male_total + stu_fem_total)*100
        stu_fem_per = stu_fem_total/(stu_male_total + stu_fem_total)*100
        print("남학생: "+str(stu_male_total)+"명 ("+str(stu_male_per)+"%)")
        print("여학생: "+str(stu_fem_total)+"명 ("+str(stu_fem_per)+"%)")
        stu_list = raw_info.getiterator("student")
        stu_major_total = 0
        stu_prac_com_languages = 0
        stu_prac_com_languages_upper = 0
        stu_python_exper = 0
        for stu in stu_list: #스튜던트 태그의 주소를 하나씩 넣는다.
            if stu.findtext("major") == "컴퓨터 공학" or "통계" in stu.findtext("major"):
                stu_major_total += 1
            if stu.find("practicable_computer_languages"):
                stu_prac_com_languages += 1
            m = stu.find("practicable_computer_languages") #값이 없어서 0이 나온다
            if not m:
                pass
            else :
                n = m.getiterator("language name")  #렝귀지 네임의 주소를 모두 찾아서
                for b in n:
                    if n.get("level") == "상":
                        stu_prac_com_languages_upper += 1
                    if n.get("name") == "python":
                        stu_python_exper += 1
        print("전공여부")
        stu_major_per = str(stu_major_total/int(stu_total)*100)
        stu_prac_com_per = str(stu_prac_com_languages/int(stu_total)*100)
        stu_prac_com_upper_per = str(stu_prac_com_languages_upper/int(stu_total)*100)
        stu_python_per = str(stu_python_exper/int(stu_total)*100)
        print("전공자(컴퓨터 공학, 통계): "+str(stu_major_total)+"명 ("+stu_major_per+"%)")
        print("프로그래밍 언어 경험자: "+str(stu_prac_com_languages)+"명 ("+stu_prac_com_per+"%)")
        print("프로그래밍 언어 상급자: "+str(stu_prac_com_languages_upper)+"명 ("+stu_prac_com_upper_per+"%)")
        print("파이썬 경험자 : " +str(stu_python_exper)+"명 ("+stu_python_per+"%)")
        age_20=0
        age_20_list=[]
        age_30=0
        age_30_list=[]
        age_40=0
        age_40_list=[]
        stu_list = raw_info.getiterator("student")
        for stu in stu_list:
            stu_age =int(stu.findtext("age"))
            if 20<=stu_age<30:
                age_20+=1
                age_20_list.append(stu.get("name")+":"+str(stu_age))
            elif 30<=stu_age<40:
                age_30+=1
                age_30_list.append(stu.get("name")+":"+str(stu_age))
            elif stu_age >= 40:
                age_40+=1
                age_40_list.append(stu.get("name")+":"+str(stu_age))
        age_20_per = str(age_20/int(stu_total)*100)
        age_30_per = str(age_30/int(stu_total)*100)
        age_40_per = str(age_40/int(stu_total)*100)
        print("*연령대")
        print("- 20대: "+str(age_20)+"("+age_20_per+"%)")
        print(" ".join(age_20_list))
        print("- 30대: "+str(age_30)+"("+age_30_per+"%)")
        print(" ".join(age_30_list))
        print("- 40대: "+str(age_40)+"("+age_40_per+"%)")
        print(" ".join(age_40_list))
    if menu_choice == "2":
        print("전체 학생 데이터")
        stu_list = raw_info.getiterator("student")
        for stu in stu_list:
            print("*"+stu.get("name"))
            print("- 성별: "+stu.get("sex"))
            print("- 나이: "+stu.findtext("age"))
            print("- 전공: "+stu.findtext("major"))
            m= stu.find("practicable_computer_languages")
            if not m:
                print("- 사용 가능한 컴퓨터 언어 : 없음")
            else:
                print("- 사용 가능한 컴퓨터 언어")
                n = m.getiterator("language")
                for b in n:
                    lang_name = b.get("name")
                    lang_level = b.get("level")
                    lang_period_raw = b.find("period")
                    lang_period = lang_period_raw.get("value")
                    print("> "+lang_name+"(학습기간: "+lang_period+", level: "+lang_level+")")
    if menu_choice == "3":
        print("학생 정보 분석 완료!")




