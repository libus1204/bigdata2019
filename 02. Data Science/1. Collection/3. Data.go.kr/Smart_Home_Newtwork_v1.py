import urllib.request
import datetime
import json
import time
import threading
import ctypes

json_weather_result=[]
yyyymmdd = time.strftime("%Y%m%d")
day_time = time.strftime("%H%M")
day_hour = time.strftime("%H")
day_min = time.strftime("%M")
x_coodinate = "89"
y_coodinate = "91"
access_key="QEbF%2Bnfi5HCWciz2PTe%2FWlO%2F1by9CxB8jfRWiyq0IZm%2BrsVxcwMDX%2FkB%2Fb7alBc21fi9EwXCounWbKTu98MDdw%3D%3D"
g_Radiator = False
g_Gas_Value = False
g_Balcony_Windows = False
g_Door = False
g_Air_Conditional = False
g_Humidifier = False
g_AI_Mode = False

def get_Request_URL(url):  # (1) 기상 정보(동네예보정보 조회 서비스 / (2) 통합대기환경 정보(대기오염정보 조회 서비스)
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

def Make_Weather_Json(day_time):  # (1) 기상정보(동네예보정보 조회 서비스) json 파일 생성하는 함수
    jsonData = get_Weather_URL(day_time)

    if (jsonData['response']['header']['resultMsg'] == 'OK'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_weather_result.append({'baseDate':prn_data.get('baseDate'), 'baseTime':prn_data.get('baseTime'),
                                        'category':prn_data.get('category'), 'fcstDate':prn_data.get('fcstDate'),
                                        'fcstTime':prn_data.get('fcstTime'), 'fcstValue':prn_data.get('fcstValue'),
                                        'nx':prn_data.get('nx'), 'ny':prn_data.get('ny')})

    with open('동구_신암동_초단기예보조회_%s%s.json' % (yyyymmdd, day_time), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(json_weather_result, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print('동구_신암동_초단기예보조회_%s_%s.json Saved\n' % (yyyymmdd, day_time))

    read_Weather()

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

def read_Weather():  # 날씨 정보 읽어오는 함수
    weather_info = []
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

        # print("\n<<가장 최신 기상정보 업데이트를 실시합니다!!>>\n".center(30))
    with open("동구_신암동_초단기예보조회_%s%s.json" % (yyyymmdd, day_time), encoding='UTF8') as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        weather_info = json.loads(json_string)
    return weather_info
    #  T1H : 기온   RN1 : 1시간 강수량   SKY : 하늘상태   UUU : 동서바람성분   VVV : 남북바람성분   REH : 습도
    #  PTY : 강수형태   LGT : 낙뢰   VEC : 풍향   WSD : 풍속

def print_main_menu():  # 메인 메뉴 출력
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")

def print_device_status(device_name, device_status): # 기기 작동 상태 확인
    print("%s 상태 : " % device_name, end="")
    if device_status == True : print("작동")
    else : print("정지")

def check_device_status():  # 기기 상태를 확인하는 함수, print_device_status 함수로 바로 가게
    print("-----------------------------------------")
    print_device_status('1. 난방기', g_Radiator)
    print_device_status('2. 가스밸브', g_Gas_Value)
    print_device_status('3. 발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('4. 에어컨 ', g_Air_Conditional)
    print_device_status('5. 가습기 ', g_Humidifier)
    print_device_status('6. 출입문 ', g_Door)
    print("-----------------------------------------")

def control_device():  # 장비 제어// 입력하면 장비의 상태가 반대로 변경

    global g_Radiator, g_Gas_Value, g_Balcony_Windows, g_Air_Conditional, g_Humdifier, g_Door
    while True:
        check_device_status()
        # print_device_status()
        print("")
        menu_num = input("상태를 변경할 기기의 번호를 입력하세요(엔터 입력시 메인 메뉴로 이동) : ")

        if menu_num == '1': g_Radiator = not g_Radiator
        if menu_num == '2': g_Gas_Value = not g_Gas_Value
        if menu_num == '3': g_Balcony_Windows = not g_Balcony_Windows
        if menu_num == '4': g_Air_Conditional = not g_Air_Conditional
        if menu_num == '5': g_Humdifier = not g_Humidifier
        if menu_num == '6': g_Door = not g_Door
        elif not menu_num:
            break
        check_device_status()

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

def ai_device_control(weather_info):
    global g_Radiator, g_Balcony_Windows, g_Air_Conditional, g_Humidifier
    temperature = 0
    humidity = 0
    rain = 0
    for temp_element in range(len(read_Weather())):
        if weather_info[temp_element]["category"] == "T1H":
            temperature = weather_info[temp_element]["fcstValue"]
            break
    for hum_element in range(len(read_Weather())):
        if weather_info[hum_element]["category"] == "REH":
            humidity = weather_info[hum_element]["fcstValue"]
            break
    for rain_element in range(len(read_Weather())):
        if weather_info[rain_element]["category"] == "RN1":
            rain = weather_info[rain_element]["fcstValue"]
            break
    print("-----------------------------------------------------------")
    print(''' * 라디에이터는 3도 이하
 * 에어컨은 31도 이상
 * 가습기는 60% 이상 자동으로 작동합니다
 * 창문(발코니는)은 열려있을 동안 비가 오면 자동으로 닫힙니다.''')
    # if temperature

def smart_mode():  # 스마트모드
    global g_AI_Mode
    print("1. 스마트모드 설명")
    print("2. 인공지능 모드 상태 확인")
    print("3. 인공지능 모드 상태 변경")
    print("4. 실시간 기상정보 Update")
    print("5. 메인 메뉴로 이동")
    print("")
    menu_num = int(input("메뉴를 선택하세요 : "))
    if menu_num == 1:
        print('''\n------------------------------------------------------
* 스마트 모드란?
    - 기온, 습도, 온도 등의 데이터를 실시간으로 받아서
      자동으로 기기들을 제어하는 모드입니다.
------------------------------------------------------''')
        print("")
        smart_mode()
    if menu_num == 2:
        print("\n현재 인공지능 모드는 ", end="")
        if g_AI_Mode == True: print("작동 중 입니다.")
        else:
            print("중지 중 입니다.")
            print("")
        smart_mode()
    if menu_num == 3:
        g_AI_Mode = not g_AI_Mode
        print("\n현재 인공지능 모드가  ", end="")
        if g_AI_Mode == True :
            print("작동 중 입니다.")
            print("")
            ai_scheduler = threading.Thread(target=update_scheduler)
            ai_scheduler.daemon = True
            ai_scheduler.start()
            get_Realtime_Weather_Info()
            ai_device_control(read_Weather())
        else:
            while ai_scheduler.is_alive():
                try:
                    terminate_ai_mode()
                except:
                    pass
            print("정지 중 입니다.")
            print("")

        smart_mode()

    elif menu_num == 4:
        get_Realtime_Weather_Info()
        print("메인 메뉴로 돌아갑니다.")
    # elif not menu_num:

def update_scheduler():  # 인공지능 모드가 True 일 때 매 시 45분 1초마다 기상 업데이트
    while True:
        if g_AI_Mode == False:
            continue
        else:
            if time.strftime('%M%S') == "4501":
                print("매 시간 기상 업데이트를 시작합니다.")
                get_Realtime_Weather_Info()
                time.sleep(5)


















print("< 스마트 홈 네트워크 시뮬레이션 프로그램 ver 1.0 >")
print("                                   - 김상민 -")
while True:
    ai_scheduler = threading.Thread(target=update_scheduler)
    ai_scheduler.daemon = True
    ai_scheduler.start()


    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요 : "))
    print("")

    if menu_num == 1:
        check_device_status()
    elif menu_num == 2:
        control_device()
    elif menu_num == 3:
        smart_mode()
    elif menu_num == 4:
        print("프로그램을 종료합니다.")
        break

# 온도 하기
