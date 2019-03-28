import urllib.request
import datetime, json, time, threading, re, sys, ctypes
from bs4 import BeautifulSoup
from selenium import webdriver
from xml.etree.ElementTree import parse
from collections import OrderedDict

app_id="Hg0dhLPJ0jH4hWnGDKk6" # 본인 ID 입력 네이버
app_pw="uv8hn6MlfZ" # 본인 Password 입력 네이버
access_key="QEbF%2Bnfi5HCWciz2PTe%2FWlO%2F1by9CxB8jfRWiyq0IZm%2BrsVxcwMDX%2FkB%2Fb7alBc21fi9EwXCounWbKTu98MDdw%3D%3D" # 공공데이터
# access_key="CYe%2BxZfEnJ0nHxomwRLowxGUT6fS623%2FB1j7%2B4AX7RZ0Itz5OoAWiKyLojAjyDrakdRp3%2BanNahGbu6aLEZYVg%3D%3D" # 공공데이터
# access_key="GMAg38HVaGoDNnGL4DtAbKle1ggqtxQU8366X1IcaPrrCH08aZkSrMf9I%2BPIXTRFpofW%2Btu%2BdkstNSL0JZTh%2BA%3D%3D"
json_weather_result=[]
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
x_coodinate = "89"
y_coodinate = "91"
json_dust_info = []

g_Radiator = False
g_Gas_Value = False
g_Balcony_Windows = False
g_Door = False
g_Air_Conditional = False
g_Humidifier = False
g_DeHumidifier = False
g_Speaker = False
g_Television = False
g_Air_Cleaner = False
g_AI_Mode = False

########### URL GET ###########
def get_Request_URL(url ):  # (1) 기상 정보(동네예보정보 조회 서비스
    req = urllib.request.Request(url)  # request 날리는 함수
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(), url))
        return None

########### 날씨 URL ###########
def get_Weather_URL(day_time):  # (1) 기상정보(동네예보정보 조회 서비스) request 보내기 전, url 만드는 함수
    end_point="http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&base_date=" + yyyymmdd
    parameters += "&base_time=" + day_time
    parameters += "&nx=" + x_coodinate
    parameters += "&ny=" + y_coodinate
    parameters += "&numOfRows=100"

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

########### 날씨 json, xml 파일 생성 ###########
def Make_Weather_Json(day_time):  # (1) 기상정보(동네예보정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)
    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate':prn_data.get('baseDate'), 'baseTime':prn_data.get('baseTime'),
                                        'category':prn_data.get('category'), 'fcstDate':prn_data.get('fcstDate'),
                                        'fcstTime':prn_data.get('fcstTime'), 'fcstValue':prn_data.get('fcstValue'),
                                        'nx':prn_data.get('nx'), 'ny':prn_data.get('ny')})

    with open('동구_신암동_초단기예보조회_%s.json' % yyyymmdd, 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    weather_for_csv = ['baseDate,baseTime,category,fcstDate,fcstTime,fcstValue,nx,ny']
    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            weather_for_csv.append(str(prn_data.get('baseDate'))+','+str(prn_data.get('baseTime'))+','+
                                 str(prn_data.get('category'))+','+str(prn_data.get('fcstDate'))+','+
                                 str(prn_data.get('fcstTime'))+','+str(prn_data.get('fcstValue'))+','+
                                 str(prn_data.get('nx'))+','+str(prn_data.get('ny')))
    f = open('동구_신암동_초단기예보조회_%s.csv' % yyyymmdd, 'w')
    f.write('\n'.join(weather_for_csv))
    f.close()
    print('동구_신암동_초단기예보조회_%s.json Saved' % yyyymmdd)
    print('동구_신암동_초단기예보조회_%s.csv Saved\n' % yyyymmdd)

########### 날씨 실시간 정보 업데이트 ###########
def get_Realtime_Weather_Info():  # (1) 기상 정보(동네예보정보 조회 서비스) json 파일 만들기 전, 실시간 업데이트 확인 함수
    day_min_int = int(day_min)
    if 30 < day_min_int <= 59 :  # 실시간 업데이트가 있는지 없는지 확인, 30분부터 59분까지는 실시간 정보 업데이트 됨
        day_time=time.strftime("%H%M", time.localtime(time.time()))
        print("\n<<실시간 기상정보 업데이트 실시합니다!!>\n".center(30))
        Make_Weather_Json(day_time)

    elif 0 <= day_min_int <= 30:  # 실시간 업데이트가 되지 않을 경우, 가장 최신인 한 시간 전 것으로
        day_hour_int = int(day_hour)
        day_hour_int = day_hour_int-1
        revised_min = 60 + (day_min_int-30)  # 정확히 30분 뺀다
        day_time = "{0:0>2}".format(day_hour_int) + str(revised_min)  # 시간이 1자리 수일때, 930 되는것을 0930으로 바꿔줌

        print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))
        Make_Weather_Json(day_time)

########### 먼지 URL ###########
def get_dust_URL():
    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?&_returnType=json&serviceKey=" + access_key
    parameters += "&sidoName=%EB%8C%80%EA%B5%AC"
    parameters += "&ver=1.3"
    parameters += "&numOfRaws=10"

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

########### 먼지 json, xml 파일 생성 ###########
def make_dust_Json():
    jsonData = get_dust_URL()
    if (jsonData['list']):
        for prn_data in jsonData['list']:
            json_dust_info.append({'stationName': prn_data.get('stationName'), 'dataTime': prn_data.get('dataTime'),
                                   'khaiGrade': prn_data.get('khaiGrade')})

    with open('동구_신암동_미세먼지_%s.json' % yyyymmdd, 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(json_dust_info, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)
    print("동구_신암동_미세먼지_%s.json Saved" % yyyymmdd)

    dust_for_csv = ['stationName, dataTime, khaiGrade']
    if (jsonData['list']):
        for prn_data in jsonData['list']:
            dust_for_csv.append(prn_data.get('stationName')+','+prn_data.get('dataTime')+','+
                                prn_data.get('khaiGrade'))

    f = open('동구_신암동_미세먼지_%s.csv' % yyyymmdd, 'w')
    f.write('\n'.join(dust_for_csv))
    f.close()
    print("동구_신암동_미세먼지_%s.csv Saved" % yyyymmdd)

########### 날씨 정보 read ###########
def read_Weather():  # 날씨 정보 읽어오는 함수
    weather_info = []
    with open("동구_신암동_초단기예보조회_%s.json" % (yyyymmdd), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        weather_info = json.loads(json_string)

    return weather_info
    #  T1H : 기온   RN1 : 1시간 강수량   SKY : 하늘상태   UUU : 동서바람성분   VVV : 남북바람성분   REH : 습도
    #  PTY : 강수형태   LGT : 낙뢰   VEC : 풍향   WSD : 풍속

########### 먼지 정보 read ###########
def read_dust():
    dust_info = []
    with open("동구_신암동_미세먼지_%s.json" % yyyymmdd, encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        dust_info = json.loads(json_string)
    return dust_info

########### 메인 메뉴 호출 ###########
def print_main_menu():  # 메인 메뉴 출력
    print("\n1. 장비 상태 확인")
    print("2. 장비 제어")
    print("3. 스마트 모드")
    print("4. 여러가지 기능")
    print("5. 약국 정보")
    print("6. 시뮬레이션")
    print("7. 프로그램 종료")

########### 장비 작동/정지 상태 호출 ###########
def print_device_status(device_name, device_status): # 기기 작동 상태 확인
    print("%s 상태 : " % device_name, end="")
    if device_status == True : print("작동")
    else : print("정지")

########### 장비 상태 확인 ###########
def check_device_status():  # 기기 상태를 확인하는 함수, print_device_status 함수로 바로 가게
    print("-----------------------------------------")
    print_device_status('1. 난방기', g_Radiator)
    print_device_status('2. 가스밸브', g_Gas_Value)
    print_device_status('3. 발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('4. 에어컨', g_Air_Conditional)
    print_device_status('5. 제습기', g_Humidifier)
    print_device_status('6. 가습기', g_DeHumidifier)
    print_device_status('7. 출입문', g_Door)
    print_device_status('8. 스피커', g_Speaker)
    print_device_status('9. TV', g_Television)
    print_device_status('10. 공기 청정기', g_Air_Cleaner)
    print("-----------------------------------------")

########### 장비 수동 제어 ###########
def control_device():  # 장비 제어// 입력하면 장비의 상태가 반대로 변경
    global g_Radiator, g_Gas_Value, g_Balcony_Windows, g_Air_Conditional, g_Humidifier
    global g_DeHumidifier, g_Door, g_Television, g_Speaker, g_Air_Cleaner
    while True:
        check_device_status()
        # print_device_status()
        print("")
        menu_num = input("상태를 변경할 기기의 번호를 입력하세요(엔터 입력시 메인 메뉴로 이동) : ")

        if menu_num == '1': g_Radiator = not g_Radiator
        if menu_num == '2': g_Gas_Value = not g_Gas_Value
        if menu_num == '3': g_Balcony_Windows = not g_Balcony_Windows
        if menu_num == '4': g_Air_Conditional = not g_Air_Conditional
        if menu_num == '5': g_Humidifier = not g_Humidifier
        if menu_num == '6': g_DeHumidifier = not g_DeHumidifier
        if menu_num == '7': g_Door = not g_Door
        if menu_num == '8': g_Speaker = not g_Speaker
        if menu_num == '9': g_Television = not g_Television
        if menu_num == '10': g_Air_Cleaner = not g_Air_Cleaner
        if not menu_num:
            break
        check_device_status()

########### 장비 AI 제어 ###########
def ai_device_control(weather_info, dust_info):
    global g_Radiator, g_Balcony_Windows, g_Air_Conditional, g_Humidifier, g_DeHumidifier, g_Air_Cleaner
    temperature = 0
    humidity = 0
    rain = 0
    air_pollution = 0
    for temp_element in range(len(weather_info)):
        if weather_info[temp_element]["category"] == "T1H":
            temperature = weather_info[temp_element]["fcstValue"]
            break
    for hum_element in range(len(weather_info)):
        if weather_info[hum_element]["category"] == "REH":
            humidity = weather_info[hum_element]["fcstValue"]
            break
    for rain_element in range(len(weather_info)):
        if weather_info[rain_element]["category"] == "RN1":
            rain = weather_info[rain_element]["fcstValue"]
            break
    for dust_element in range(len(dust_info)):
        if dust_info[dust_element]['stationName'] == '신암동':
            air_pollution = dust_info[dust_element]['khaiGrade']
    print("\n -- 장비 제어를 시작합니다 -- ")
    print("")
    time.sleep(2)
    print("-----------------------------------------------------------------")
    print(''' * 라디에이터는 실외 "3℃" 이하
 * 에어컨은 실외 "31℃" 이상
 * 제습기는 "60%" 이상 
 * 제습기는 "60%" 이상
 * 가습기는 "35%" 이하
 * 공기청정기는 통합대기환경지수가 "2(보통)" 이상 일 경우 작동합니다.
 * 창문(발코니는)은 열려 있는 동안 비가 오면 자동으로 닫힙니다.
 * 또한 메인 메뉴에서 수동으로 모든 기기 제어가 가능합니다.
 -----------------------------------------------------------------''')
    print("")
    time.sleep(2)
    print('''현재 기상 상태는
기온 %s 도, 습도 %s %%, 강수량 %s mm, 통합대기환경지수 %s 입니다.''' % (temperature, humidity, rain, air_pollution))
    if temperature <= 3:
        if g_Radiator == False:
            g_Radiator = not g_Radiator
            print("\n라디에이터 작동을 시작합니다.")
        else: pass
    if temperature >= 31:
        if g_Air_Conditional == False:
            g_Air_Conditional = not g_Air_Conditional
            print("\n에어컨이 작동을 시작합니다.")
        else: pass
    if int(humidity) <= 35:
        if g_DeHumidifier == False:
            g_DeHumidifier = not g_DeHumidifier
            print("\n가습기 작동을 시작합니다.")
        else: pass
    if int(humidity) >= 60 :
        if g_Humidifier == False:
            g_Humidifier = not g_Humidifier
            print("\n제습기 작동을 시작합니다.")
    if int(rain) > 0:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = not g_Balcony_Windows
            print("\n창문을 닫습니다.")
        else: pass
    if int(air_pollution) >= 2:
        if g_Balcony_Windows == True:
            g_Balcony_Windows = not g_Balcony_Windows
            print("\n창문을 닫습니다")
            if g_Air_Cleaner == False:
                print("\n공기청정기를 작동을 시작합니다.")
                g_Air_Cleaner = not g_Air_Cleaner
        else:
            if g_Air_Cleaner == False:
                print("\n공기청정기를 작동을 시작합니다.")
                g_Air_Cleaner = not g_Air_Cleaner

########### 아침 7시 기상정보 알람 ###########
def morning_alram(weather_info, dust_info):
    temperature = 0
    air_pollution = 0
    rain = 0
    for temp_element in range(len(read_Weather())):
        if weather_info[temp_element]["category"] == "T1H":
            temperature = weather_info[temp_element]["fcstValue"]
            break
    for rain_element in range(len(read_Weather())):
        if weather_info[rain_element]["category"] == "RN1":
            rain = weather_info[rain_element]["fcstValue"]
            break
    for dust_element in range(len(read_dust())):
        if dust_info[dust_element]["stationName"] == "신암동":
            air_pollution = dust_info[dust_element]["khaiGrade"]
    print("현재 기온은 %s 도, 강수량은 %s mm, 통합대기환경지수는 %s 입니다." % (temperature, rain, air_pollution))
    if int(rain) > 1:
        print("밖에 비가 내리니 우산을 챙기세요~^^")
    if int(air_pollution) >= 2:
        print("밖에 공기가 좋지 않으니 마스크 꼭 챙기세요~^^")

def terminate_ai_mode():
    """Terminates a python thread from another thread.
    :param thread: a threading.Thread instance
    """
    if not ai_scheduler.isAlive():
        return

    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(ai_scheduler.ident), exc)
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ai_scheduler.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed.")

########### 스케쥴러 ###########
def update_scheduler():
    global g_Television
    while True:
        if g_AI_Mode == False:
            continue
        elif time.strftime('%M%S') == "4602":   # 인공지능 모드가 True 일 때 매 시 45분 31초마다 기상 업데이트
            time.sleep(3)
            print("\n매 시간 기상 업데이트를 시작합니다.")
            get_Realtime_Weather_Info()
            make_dust_Json()
            ai_device_control(read_Weather(), read_dust())
            print("\n업데이트가 끝났습니다.\n이전 하던 작업을 계속 진행하세요.")
            # print_main_menu()
        elif time.strftime('%H%M%S') == "070000":  # 아침 7시마다 기온, 강수량, 공기오염도 알람
            get_Realtime_Weather_Info()
            time.sleep(3)
            if g_Television == False: g_Television = not g_Television
            else: continue
            morning_alram(read_Weather())

########### 스마트모드 ###########
def smart_mode():  # 스마트모드
    global g_AI_Mode
    print("1. 스마트 모드 설명")
    print("2. 인공지능 모드 상태 확인")
    print("3. 인공지능 모드 상태 변경")
    print("4. 실시간 기상정보 Update")
    print("")
    menu_num = input("메뉴를 선택하세요(엔터 시 메인메뉴로 이동) : ")
    if menu_num == '1':
        print('''\n------------------------------------------------------
* 스마트 모드란?
    - 기온, 습도, 온도 등의 데이터를 실시간으로 받아서
      자동으로 기기들을 제어하는 모드입니다.
      매 시간 45분 또는 실시간 기상정보 Update 를 통해
      각각의 기기를 자동으로 제어할 수 있습니다.
------------------------------------------------------''')
        print("")
        smart_mode()
    if menu_num == '2':
        print("\n현재 인공지능 모드는 ", end="")
        if g_AI_Mode == True: print("작동 중 입니다.")
        else:
            print("중지 중 입니다.")
            print("")
        smart_mode()
    if menu_num == '3':
        ai_scheduler = threading.Thread(target=update_scheduler)
        ai_scheduler.daemon = True
        g_AI_Mode = not g_AI_Mode
        print("\n현재 인공지능 모드가  ", end="")
        if g_AI_Mode == True :
            print("작동 중 입니다.")
            print("")
            ai_scheduler.start()
            pass
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass
            print("정지 중 입니다.")
            print("")
    elif menu_num == '4':
        get_Realtime_Weather_Info()
        make_dust_Json()
        ai_device_control(read_Weather(), read_dust())
    elif not menu_num: pass

########### 네이버 url get ###########
def get_request_url_naver(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", app_id)
    req.add_header("X-Naver-Client-Secret", app_pw)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            # print("[%s] Url:%s => Request Success" % (datetime.datetime.now(), url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

########### 네이버 검색 함수 ###########
def getNaverSearchResult(sNode, search_text, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % sNode
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text), page_start, display)
    url = base+node+parameters
    retData = get_request_url_naver(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

########### 네이버 블로그 포스팅 겟 ###########
def getPostData_blog(post, jsonResult):
    # Data Sampling
    title = post['title']
    bloggername = post['bloggername']
    link = re.sub("\?Redirect=Log&amp;logNo=", '/', post['link'])
    description = post['description']
    postdate = post['postdate']
    # 데이터 가공/보정
    jsonResult.append({'title':title, 'bloggername':bloggername, 'link':link, 'description':description,
                       'postdate':postdate})
    return

########### 네이버 블로그 검색 ###########
def naver_blog_search(search_text):
    jsonResult = []
    sNode = 'blog'

    print("\n외부 빅데이터를 수집합니다.")
    display_count = 10

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

    index = 1

    while((jsonSearch!=None) and (jsonSearch['display']!=0) and index<6):
        for post in jsonSearch['items']:
            getPostData_blog(post, jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
        index = index+1

    with open('%s_naver_%s.json' %(search_text, sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4,sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    return search_text

########### 네이버 블로그 검색 결과 호출 ###########
def naver_blog_print(search_text):
    naver_blog_data = []
    list_title=[]
    with open("%s_naver_%s.json" % (search_text, 'blog'), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        naver_blog_data = json.loads(json_string)
    naver_blog_count = len(naver_blog_data)
    p = re.compile(r'<.?b>')
    for count in range(naver_blog_count):
        list_title.append(naver_blog_data[count]["title"])
    for i in range(len(list_title)):
        real_title = re.sub(p, "", list_title[i])
        list_title[i] = real_title
    print("%s 검색어에 대한 50개의 블로그 검색 결과를 출력합니다." % search_text)
    for blog_post_count in range(naver_blog_count):
        print("\n블로그 제목 : %s" % list_title[blog_post_count])
        print("블로그 일자 : %s" % naver_blog_data[blog_post_count]["postdate"])
        print("블로그 링크 : %s" % naver_blog_data[blog_post_count]["link"])

########### 네이버 뉴스 기사 겟 ###########
def getPostData_news(post, jsonResult):
    # Data Sampling
    title = post['title']
    description = post['description']
    org_link = post['originallink']
    # 데이터 가공/보정
    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'title':title, 'description':description, 'org_link':org_link, 'pDate':pDate})
    return

########### 네이버 뉴스 검색 ###########
def naver_news_search(search_text):
        jsonResult = []

        sNode = 'news'

        print("\n외부 빅데이터를 수집합니다.")
        display_count = 10

        jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

        index = 1 # 1번 루프를 돌 때 마다 100건이 조회되기 때문에 1000번을 넘기지 않게 하기 위한 인덱스

        while((jsonSearch!=None) and (jsonSearch['display']!=0) and index<6):
            for post in jsonSearch['items']:
                getPostData_news(post, jsonResult)

            nStart = jsonSearch['start'] + jsonSearch['display']
            jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
            index = index+1

        with open('%s_naver_%s.json' %(search_text, sNode), 'w', encoding='utf8') as outfile:
            retJson = json.dumps(jsonResult, indent=4,sort_keys=True, ensure_ascii=False)
            outfile.write(retJson)

########### 네이버 뉴스 검색 결과 호출 ###########
def naver_news_print(search_text):
    naver_news_data = []
    list_title = []
    list_describ = []
    with open("%s_naver_%s.json" % (search_text, 'news'), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        naver_news_data = json.loads(json_string)
    naver_news_count = len(naver_news_data)
    p = re.compile(r'<.?b>')
    for count in range(naver_news_count):
        list_title.append(naver_news_data[count]["title"])
        list_describ.append(naver_news_data[count]["description"])
    for i in range(len(list_title)):
        real_title = re.sub(p, "", list_title[i])
        real_article = re.sub(p, "", list_describ[i])
        list_title[i] = real_title
        list_describ[i] = real_article
    print("%s 검색어에 대한 50개의 뉴스 검색 결과를 출력합니다." % search_text)
    for news_article_count in range(naver_news_count):
        print("\n제목 : %s" % list_title[news_article_count])
        print("일자 : %s" % naver_news_data[news_article_count]["pDate"])
        print("내용 : %s..." % list_describ[news_article_count][0:50])
        print("링크 : %s" % naver_news_data[news_article_count]["org_link"])

########### 네이버 실시간 뉴스 ###########
def naver_news_rankup():
    html = urllib.request.urlopen('https://news.naver.com')
    soup = BeautifulSoup(html, 'html.parser')
    tags = str(soup)
    news_politic = []
    news_economy = []
    news_social = []
    news_life = []
    news_world = []
    news_science = []
    news_politic_url = []
    news_economy_url = []
    news_social_url = []
    news_life_url = []
    news_world_url = []
    news_science_url = []
    p_title = re.compile(r'nclicks.*>\n<strong>(.*)</strong>')
    for i in range(len(p_title.findall(tags))):
        if i >= 0 and i <= 4:
            news_politic.append(p_title.findall(tags)[i])
        elif i >= 5 and i <= 9:
            news_economy.append(p_title.findall(tags)[i])
        elif i >= 10 and i <= 14:
            news_social.append(p_title.findall(tags)[i])
        elif i >= 15 and i <= 19:
            news_life.append(p_title.findall(tags)[i])
        elif i >= 20 and i <= 24:
            news_world.append(p_title.findall(tags)[i])
        elif i >= 25 and i <= 29:
            news_science.append(p_title.findall(tags)[i])

    p_url = re.compile(r'" href="(.*nhn[?]mode=LSD&amp;mid=shm&amp;sid1=.*&amp.*)">\n')
    list = p_url.findall(tags)
    list2 = []
    for i in list:
        a = i.replace('amp;', '')
        list2.append(a)
    for i in range(len(list2)):
        if i >= 1 and i <= 5:
            news_politic_url.append(list2[i])
        elif i >= 7 and i <= 11:
            news_economy_url.append(list2[i])
        elif i >= 13 and i <= 17:
            news_social_url.append(list2[i])
        elif i >= 19 and i <= 23:
            news_life_url.append(list2[i])
        elif i >= 25 and i <= 29:
            news_world_url.append(list2[i])
        elif i >= 31 and i <= 35:
            news_science_url.append(list2[i])
    print("\n1.정치\n2.경제\n3.사회\n4.생활/문화\n5.세계\n6.IT/과학")
    news_want = input("\n카테고리를 선택하세요. : ")
    print("")
    if news_want == '1':
        for count in range(5):
            print("%s. %s [%s]" % (count + 1, news_politic[count], news_politic_url[count]))
    elif news_want == '2':
        for count in range(5):
            print("%s. %s [%s]" % (count + 1, news_economy[count], news_economy_url[count]))
    elif news_want == '3':
        for count in range(5):
            print("%s. %s [%s]" % (count + 1, news_social[count], news_social_url[count]))
    elif news_want == '4':
        for count in range(5):
            print("%s. %s [%s]" % (count + 1, news_life[count], news_life_url[count]))
    elif news_want == '5':
        for count in range(5):
            print("%s. %s [%s]" % (count + 1, news_world[count], news_world_url[count]))
    elif news_want == '6':
        for count in range(5):
            print("%s. %s [%s]" % (count + 1, news_science[count], news_science_url[count]))

########### 네이버 쇼핑 겟 ###########
def getPostData_shop(post, jsonResult):
    # Data Sampling
    title = post['title']
    link = post['link']
    lprice = post['lprice']
    hprice = post['hprice']
    mallName = post['mallName']
    productType = post['productType']

    jsonResult.append({'title':title, 'link':link, 'lprice':lprice, 'hprice':hprice,
                       'mallName':mallName, 'productType':productType})
    return

########### 네이버 쇼핑 검색 ###########
def naver_shop_search(search_text):
    jsonResult = []

    sNode = 'shop'
    print("\n외부 빅데이터를 수집합니다.")
    display_count = 10

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

    index = 1 # 1번 루프를 돌 때 마다 100건이 조회되기 때문에 1000번을 넘기지 않게 하기 위한 인덱스

    while((jsonSearch!=None) and (jsonSearch['display']!=0) and index<6):
        for post in jsonSearch['items']:
            getPostData_shop(post, jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
        index = index+1

    with open('%s_naver_%s.json' %(search_text, sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4,sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

########### 네이버 쇼핑 검색 결과 호출 ###########
def naver_shop_print(search_text):
    naver_shop_data = []
    list_title = []
    list_describ = []
    with open("%s_naver_%s.json" % (search_text, 'shop'), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        naver_shop_data = json.loads(json_string)
    naver_shop_count = len(naver_shop_data)
    p = re.compile(r'<.?b>')
    for count in range(naver_shop_count):
        list_title.append(naver_shop_data[count]["title"])
    for i in range(len(list_title)):
        real_title = re.sub(p, "", list_title[i])
        list_title[i] = real_title
    print("%s 검색어에 대한 50개의 쇼핑 검색 결과를 출력합니다." % search_text)
    for shop_item_count in range(naver_shop_count):
        print("\n상품 이름 : %s" % list_title[shop_item_count])
        print("상품 판매 : %s" % naver_shop_data[shop_item_count]["mallName"])
        print("최저 가격 : %s" % naver_shop_data[shop_item_count]["lprice"])
        print("최고 가격 : %s" % naver_shop_data[shop_item_count]["hprice"])
        print("최고 가격 : %s" % naver_shop_data[shop_item_count]["link"])

########### 네이버 번역 ###########
def naver_translate():
    import re
    import urllib.request
    while True:
        print("1. 한국어 -> 영어\n2. 영어 -> 한국어(미구현;;)")
        menu_trans = input("번호를 선택하세요(엔터 입력시 메인화면으로 이동)  : ")
        if not menu_trans:
            break
        search_text = input("문장을 입력하세요(엔터 입력시 메인화면으로 이동) : ")
        if menu_trans == '1':
            client_id = "p2ozsJyzL8ER670ZY5of"  # 개발자센터에서 발급받은 Client ID 값
            client_secret = "3LlDySN6hR"  # 개발자센터에서 발급받은 Client Secret 값
            # text = input("번역할 단어 입력 : ")
            encText = urllib.parse.quote(search_text)
            data = "source=ko&target=en&text=" + encText
            url = "https://openapi.naver.com/v1/papago/n2mt"
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(request, data=data.encode("utf-8"))
            rescode = response.getcode()
            if (rescode == 200):
                response_body = response.read()
                list_result = str(response_body)
                p = re.compile(r'translatedText":"(.*)"')
                m = p.findall(list_result)[0]
                p2 = re.compile(r'[\\]')
                real_trans = re.sub(p2, "", m)
                m = real_trans
                print(m)
            else:
                print("Error Code:" + rescode)
        elif menu_trans == '2':
            client_id = "p2ozsJyzL8ER670ZY5of"  # 개발자센터에서 발급받은 Client ID 값
            client_secret = "3LlDySN6hR"  # 개발자센터에서 발급받은 Client Secret 값
            # text = input("번역할 단어 입력 : ")
            encText = urllib.parse.quote(search_text)
            data = "source=en&target=ko&text=" + encText
            url = "https://openapi.naver.com/v1/papago/n2mt"
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(request, data=data.encode("utf-8"))
            rescode = response.getcode()
            if (rescode == 200):
                response_body = response.read()
                list_result = str(response_body)
                p = re.compile(r'translatedText":"(.*)"')
                m = p.findall(list_result)[0]
                p2 = re.compile(r'[\\]')
                real_trans = re.sub(p2, "", m)
                m = real_trans
                print(m)
            else:
                print("Error Code:" + rescode)
        if not search_text:
            break

########### 네이버 음악 ###########
def naver_music():
    global g_Speaker
    print("1. TOP 10 국내\n2. TOP 10 해외")
    menu_music = input("번호를 선택하세요 : ")
    print("")
    if menu_music == '1':
        html = urllib.request.urlopen('https://music.naver.com/listen/top100.nhn?domain=DOMESTIC_V2')
        soup = BeautifulSoup(html, 'html.parser')
        tags = str(soup)
        korean_sing_title_list = []
        korean_singer_list = []
        p_korean_title = re.compile(r'class="_title title.*title=".*psis">(.*)</span>')
        for titles in p_korean_title.findall(tags):
            korean_sing_title_list.append(titles)
        p_korean_singer = re.compile(r'" title="(.*)">\n')
        for singer in p_korean_singer.findall(tags):
            if singer == '자동완성 펼치기':
                pass
            else:
                korean_singer_list.append(singer)
        for count in range(1,11):
            print("%s. %s - %s" % (count, korean_sing_title_list[count], korean_singer_list[count]))
        p_korean_artist = re.compile(r'" href="(.*)" title=".*">\n')
        artist_info = p_korean_artist.findall(tags)
        music_url = "https://music.naver.com"
        print("아티스트 정보를 보시려면 번호를 눌러주세요 : ",end="")
        artist_select = input("")
        print("아티스트 정보 : %s" % (music_url+artist_info[int(artist_select)+1]))
    if menu_music == '2':
        html = urllib.request.urlopen('https://music.naver.com/listen/top100.nhn?domain=OVERSEA_V2')
        soup = BeautifulSoup(html, 'html.parser')
        tags = str(soup)
        pop_title_list = []
        pop_singer_list = []
        p_pop_title = re.compile(r'<span class="ellipsis">(.*)</span></a>')
        for pop_titles in p_pop_title.findall(tags):
            pop_title_list.append(pop_titles)
        p_pop_singer = re.compile(r'" title="(.*)">\n')
        for pop_singer in p_pop_singer.findall(tags):
            if pop_singer == '자동완성 펼치기':
                pass
            else:
                pop_singer_list.append(pop_singer)
        for count in range(1,11):
            print("%s. %s - %s" % (count, pop_title_list[count], pop_singer_list[count]))
        p_pop_artist = re.compile(r'" href="(.*)" title=".*">\n')
        artist_info = p_pop_artist.findall(tags)
        music_url = "https://music.naver.com"
        print("아티스트 정보를 보시려면 번호를 눌러주세요 : ",end="")
        artist_select = input("")
        print("아티스트 정보 : %s" % (music_url+artist_info[int(artist_select)+1]))
    menu_music_play = input("스피커를 통해 재생하시겠습니까? (Y/N) :  ")
    if menu_music_play == 'Y':
        print("\n스피커를 통해 TOP 10 재생을 시작합니다.") # 실제 재생은 어떻게? ㅠㅠㅠ
        if g_Speaker == False:
            g_Speaker = not g_Speaker
            print("\n스피커를 실행합니다.")
        else: pass
    else: pass

########### 네이버 실검 ###########
def naver_rankup():
    print('\n네이버 실시간 검색어 TOP 20')
    html = urllib.request.urlopen('https://www.naver.com/')
    soup = BeautifulSoup(html, 'html.parser')

    list = soup.findAll('span', attrs={"class": "ah_k"})
    for count in range(1, 21):
        print("%s. " % count + list[count].text)

    print("검색할 번호를 입력해주세요 : ", end="")
    search_input = int(input(""))
    url_search = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
    keywords = list[int(search_input)].text
    search_site = url_search + "%s" % str(keywords)
    # key_encode =
    new_screen = input("새 창으로 띄우시겠습니까? (Y/N) : ")
    if new_screen == 'N':
        print(url_search+"%s" % (str(keywords)))
    else:
        driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
        driver.implicitly_wait(1)
        driver.get(search_site)

########### 유튜브 실시간 인기 동영상 ###########
def youtube_rank():
    comment = "유튜브 실시간 인기 동영상 목록을 불러오는 중 입니다."
    for i in range(4):
        sys.stdout.write("\r" + comment + "."*i)
        sys.stdout.flush()
        time.sleep(1)
    print("")
    html = urllib.request.urlopen('https://www.youtube.com/feed/trending')
    soup = BeautifulSoup(html, 'html.parser')
    tags = str(soup)
    p = re.compile(
        r'<a aria-describedby=.*" class=".*" data-sessionlink=".*" dir=".*" href="(.*)" title="(.*)">.*</a><span class="accessible-')

    for count in range(0, 20):
        print("%s. %s" % (count + 1, p.findall(tags)[count][1]))

    print("\n시청할 동영상의 번호를 입력해주세요 : ", end="")
    search_input = int(input(""))
    url_search = "https://www.youtube.com"
    keywords = p.findall(tags)[int(search_input) - 1][0]
    search_site = url_search + keywords
    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')
    driver.implicitly_wait(1)
    driver.get(search_site)

########### 인스타 해쉬태그 검색 ###########
def instagram():
    print("해쉬태그 검색어를 입력해주세요 : ", end="")
    tag = input("#")
    comment = "인스타그램 게시글을 불러오는 중 입니다."
    for i in range(4):
        sys.stdout.write("\r" + comment + "."*i)
        sys.stdout.flush()
        time.sleep(1)
    url = 'https://m.instagram.com/explore/tags/' + tag

    driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')

    driver.implicitly_wait(5)
    driver.get(url)

########### 스팀/온라인 게임 순위 ###########
def game():
    print("게임 순위\n1. 스팀게임\n2. 온라인 게임")
    menu_game = input("번호를 선택하세요 : ")
    if menu_game == '1':
        html = urllib.request.urlopen("https://store.steampowered.com/search/?filter=topsellers")
        soup = BeautifulSoup(html, 'html.parser')
        tags = str(soup)
        game_title = []
        p_game_title = re.compile('<span class="title">(.*)</span>')
        for count in range(len(p_game_title.findall(tags))):
            game_title.append(p_game_title.findall(tags)[count])
        game_discount = []
        p_discount = re.compile('<div class="col search_discount responsive_secondrow">\n(.*)')
        p_discount_again = re.compile('<span>(-\d\d%)</span')
        for count2 in range(len(p_discount.findall(tags))):
            if not p_discount_again.findall(p_discount.findall(tags)[count2]):
                game_discount.append('0')
            else:
                game_discount.append(p_discount_again.findall(p_discount.findall(tags)[count2]))
        game_price = []
        p_price = re.compile(r'\b([0-9]+[,][0-9]+)\t')
        for count3 in p_price.findall(tags):
            game_price.append(count3)
        print("\n ===== 스팀 게임 =====")
        print("현 스팀 게임 순위, 할인율, 현재 가격")
        for count4 in range(len(game_title)):
            print("%s. %-53s %-5s %-6s " %(count4+1, game_title[count4], game_discount[count4][0], game_price[count4]))
    elif menu_game == '2':
        print("\n ===== 온라인 게임 =====")
        print("게임 순위, 사이트")
        html = urllib.request.urlopen("http://www.online-gameranking100.com/bbs/board.php?bo_table=online")
        soup = BeautifulSoup(html, 'html.parser')
        tags = str(soup)
        online_game_title = []
        p_online_title = re.compile(r'id=\d\d\d"><span>(.*)</span></a>')
        for count in range(len(p_online_title.findall(tags))):
            online_game_title.append(p_online_title.findall(tags)[count])
        online_game_site = []
        p_online_site = re.compile(r'bookmarksite.*(http.*'')[)]')
        for count2 in range(len(p_online_site.findall(tags))):
            online_game_site.append(p_online_site.findall(tags)[count2])

        for order in range(10):
            print("%s. %s [%s]" % (order+1, online_game_title[order], online_game_site[order][0:-1]))

########### 긴급서비스 검색(공공데이터 오픈api xml 이용) ###########
def emergency():
    global access_key
    # 아직 약국밖에 ㅠㅠ
    print("대구광역시 동구 신암동에 소재한 약국을 검색합니다.")
    class GetData:
        end_point = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire"
        parameters = "?&serviceKey=" + access_key
        parameters += "&Q0=%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C"
        parameters += "&Q1=%EB%8F%99%EA%B5%AC"
        parameters += "&numOfRows=100"
        url = end_point + parameters

        def main(self):
            data = urllib.request.urlopen(self.url).read()
            f = open('동구_약국.xml', 'wb')
            f.write(data)
            f.close()

    getData = GetData()
    getData.main()
    tree = parse('동구_약국.xml')
    root = tree.getroot()
    pharmacy_name = []
    pharmacy_phone = []
    pharmacy_addr = []
    for a in root.getiterator("body"):
        for b in a.getiterator("items"):
            pharmacy_tags = b.findall("item")
    for i in range(len(pharmacy_tags)):
        if '신암' in pharmacy_tags[i].findtext("dutyAddr"):
            pharmacy_name.append(pharmacy_tags[i].findtext("dutyName"))
            pharmacy_addr.append(pharmacy_tags[i].findtext("dutyAddr"))
            pharmacy_phone.append(pharmacy_tags[i].findtext("dutyTel1"))
    for count in range(len(pharmacy_name)):
        print("%s. %s\n - %s (%s)" % (count+1, pharmacy_name[count], pharmacy_addr[count], pharmacy_phone[count]))

########### 여러가지 기능 메뉴 호출 ###########
def function_mode():
    global g_Television

    print("여러 가지 기능을 실행합니다.")

    if g_Television == False:
        print("\n원활한 기능 실행을 위해 TV 를 작동시키겠습니까? (Y/N) : ", end="")
        menu_tv_on = input("")
        if menu_tv_on == 'Y':
            g_Television = not g_Television
            print("\nTV를 작동 합니다.")
        else: print("\nTV를 작동 하지 않고 기능을 실행합니다.")
    else: pass

    print("\n0. 실시간 검색\n1. 뉴스\n2. 맛집(블로그 검색)\n3. 쇼핑\n4. 번역\n5. 뮤직\n6. 유튜브 실시간 인기 동영상", end="")
    print("\n7. 인스타그램 해쉬태그 검색\n8. 게임")
    print("0 ~ 5 번은 네이버 서비스를 기반으로 합니다.")

    user_input = input(" \n원하시는 검색 종류의 번호를 선택하세요.(엔터시 메인메뉴로 이동) : ")
    if user_input == '1':
        print("\n1. 실시간 뉴스\n2. 뉴스 검색")
        menu_news = input("번호를 선택하세요 : ")
        if menu_news == '1':
            naver_news_rankup()
        if menu_news == '2':
            search_text = input("검색어를 입력하세요 : ")
            naver_news_search(search_text)
            naver_news_print(search_text)
    elif user_input == '2':
        print("\n============  맛집을 검색하세요!  =============")
        search_text = input("검색어를 입력하세요 : ")
        naver_blog_search(search_text)
        naver_blog_print(search_text)
    elif user_input == '3':
        print("\n============  상품을 검색하세요!  =============")
        search_text = input("검색어를 입력하세요 : ")
        naver_shop_search(search_text)
        naver_shop_print(search_text)
    elif user_input == '4':
        naver_translate()
    elif user_input == '5':
        naver_music()
    elif user_input == '0':
        naver_rankup()
    elif user_input == '6':
        youtube_rank()
    elif user_input == '7':
        instagram()
    elif user_input == '8':
        game()
    elif not user_input: pass

########### 시뮬레이션 입력값 json 파일 생성 ###########
def simulator_make_json():
    print("가상데이터로 기기들의 제어를 시작합니다.")
    sim_baseDate = input("날짜를 입력하세요(YYYYMMDD) : ")
    sim_baseTime = input("측정시간을 입력하세요(hhMM) : ")
    sim_category_T1H = input("온도를 입력하세요 : ")
    sim_category_RN1 = input("강수량을 입력하세요 : ")
    sim_category_REH = input("습도를 입력하세요 : ")
    sim_fcstTime = input("예측시간을 입력하세요 : ")
    sim_nx = input("위도를 입력하세요 : ")
    sim_ny = input("경도를 입력하세요 : ")
    sim_khaiGrade = input("통합대기환경지수를 입력하세요 : ")
    sim_stationName = input("동네 이름을 입력하세요 : ")
    total_air_simul = []
    total_dust_simul = []
    value = []
    value.append(sim_category_T1H)
    value.append(sim_category_RN1)
    value.append(sim_category_REH)
    category_list = ["T1H", "RN1", "REH"]
    simulation1 = OrderedDict()
    simulation2 = OrderedDict()
    simulation3 = OrderedDict()
    simulation1["baseDate"] = int(sim_baseDate)
    simulation1["baseTime"] = int(sim_baseTime)
    simulation1["category"] = str(category_list[0])
    simulation1["fcstTime"] = int(sim_fcstTime)
    simulation1["fcstValue"] = int(sim_category_T1H)
    simulation1["sim_nx"] = int(sim_nx)
    simulation1["sim_ny"] = int(sim_ny)
    simulation2["baseDate"] = int(sim_baseDate)
    simulation2["baseTime"] = int(sim_baseTime)
    simulation2["category"] = str(category_list[1])
    simulation2["fcstTime"] = int(sim_fcstTime)
    simulation2["fcstValue"] = int(sim_category_RN1)
    simulation2["sim_nx"] = int(sim_nx)
    simulation2["sim_ny"] = int(sim_ny)
    simulation3["baseDate"] = int(sim_baseDate)
    simulation3["baseTime"] = int(sim_baseTime)
    simulation3["category"] = str(category_list[2])
    simulation3["fcstTime"] = int(sim_fcstTime)
    simulation3["fcstValue"] = int(sim_category_REH)
    simulation3["nx"] = int(sim_nx)
    simulation3["ny"] = int(sim_ny)
    total_air_simul.append(simulation1)
    total_air_simul.append(simulation2)
    total_air_simul.append(simulation3)

    with open('simul_air.json', 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(total_air_simul, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    simulation4 = OrderedDict()
    simulation4["dateTime"] = sim_baseDate + sim_baseTime
    simulation4["khaiGrade"] = sim_khaiGrade
    simulation4["stationName"] = sim_stationName
    total_dust_simul.append(simulation4)

    with open('simul_dust.json', 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(total_dust_simul, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    simulation_air_csv = ["baseDate, baseTime, category, fcstTime, fcstValue, sim_nx, sim_ny"]
    for count in range(len(category_list)):
        simulation_air_csv.append(
            sim_baseDate + ',' + sim_baseTime + ',' + category_list[count] + ',' + sim_fcstTime + ',' + value[
                count] + ',' + sim_nx + ',' + sim_ny)

    f = open('simul_air_csv.csv', 'w')
    f.write('\n'.join(simulation_air_csv))
    f.close()

    simulation_dust_csv = ["stationName, dataTime, khaiGrade"]
    simulation_dust_csv.append(sim_stationName+','+sim_baseDate+sim_baseTime+','+sim_khaiGrade)

    f = open('simul_dust_csv.csv', 'w')
    f.write('\n'.join(simulation_dust_csv))
    f.close()

########### 시뮬레이션 입력값 ai 함수에 넣기 ###########
def read_simul():
    air_simul = []
    with open("simul_air.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        air_simul = json.loads(json_string)

    dust_simul = []
    with open("simul_dust.json", encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        dust_simul = json.loads(json_string)
    print("\n시뮬레이터를 시작합니다.")
    ai_device_control(air_simul, dust_simul)
    print("\n시뮬레이션을 종료합니다.")




print("< 스마트 홈 네트워크 시뮬레이션 프로그램 ver 1.0 >")
print("                                   - 김상민 -")
while True:
    print_main_menu()
    menu_num = input("메뉴를 선택하세요 : ")
    print("")

    if menu_num == '1':
        check_device_status()
    elif menu_num == '2':
        control_device()
    elif menu_num == '3':
        smart_mode()
    elif menu_num == '4':
        function_mode()
    elif menu_num == '5':
        emergency()
    elif menu_num == '7':
        print("프로그램을 종료합니다.")
        break
    elif menu_num == '6':
        simulator_make_json()
        read_simul()
    elif not menu_num: pass
