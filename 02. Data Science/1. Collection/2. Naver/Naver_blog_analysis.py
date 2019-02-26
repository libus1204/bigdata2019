import json
g_json_big_data = []
print("================ 빅데이터 분석기 =================")
user_want_anal = input("분석 키워드를 입력하세요 : ")
with open("%s_naver_%s.json" %(user_want_anal, 'news'), encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    g_json_big_data = json.loads(json_string)
news_count = len(g_json_big_data)
not_org_link_count = 0
org_domain_list = []
print("\n데이터 분석을 시작합니다...")
for count in range(news_count):  #  org_link 의 데이터가 깨져 있는지 확인
    if not g_json_big_data[count]["org_link"]:
        not_org_link_count += 1  # 깨져 있을 시 + 1
        print("'org_link'가 없는 기사를 발견했습니다.")
        pass
    else:
        org_domain_list.append(((g_json_big_data[count]["org_link"].split("//"))[1].split("/"))[0])
set_org_domain_list = set(org_domain_list)
org_domain_list_again = list(set_org_domain_list)
print("\n<네이버 검색 빅데이터 분석>")
print("검색어 : %s" % user_want_anal)
print("전체 도메인 수 : %s" % len(set_org_domain_list))
print("전체 건수 : %s" % (news_count-not_org_link_count))
print("부정확한 데이터 수 : %s" % not_org_link_count)
sort_domain_name = []
sort_domain_count = []
print("\n- 도메인 별 뉴스 기사 분석")
for count in range(len(set_org_domain_list)):
    sort_domain_name.append(org_domain_list_again[count])
    sort_domain_count.append(org_domain_list.count(org_domain_list_again[count]))
domain_dict = dict(zip(sort_domain_name, sort_domain_count))
for domain_name, domain_count in sorted(domain_dict.items(), key=lambda domain_dict:domain_dict[1], reverse=True):
    print(" >> %s : %s건" %(domain_name, domain_count))

print("분석을 완료합니다.")