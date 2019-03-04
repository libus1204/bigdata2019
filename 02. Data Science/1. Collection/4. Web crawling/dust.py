import urllib.request
import datetime
import json, time

access_key="QEbF%2Bnfi5HCWciz2PTe%2FWlO%2F1by9CxB8jfRWiyq0IZm%2BrsVxcwMDX%2FkB%2Fb7alBc21fi9EwXCounWbKTu98MDdw%3D%3D"

def get_Request_URL(url):
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

def get_dust_URL():
    end_point="http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

    parameters = "?&_returnType=json&serviceKey=" + access_key
    parameters += "&sidoName=%EB%8C%80%EA%B5%AC"
    parameters += "&ver=1.3"

    url = end_point + parameters
    retData = get_Request_URL(url)
    if (retData == None):
        return None
    else:
        return json.loads(retData)

def make_dust_Json():
    jsonData = get_dust_URL()
    if (jsonData['response']['header']['resultMsg'] == 'NORMAL SERVICE.'):
        for prn_data in jsonData['response']['body']['items']['item']:
            json_dust_info.append({'stationName':prn_data.get('stationName'), 'dataTime':prn_data.get('dataTime'),
                                   'pm10Value':prn_data.get('pm10Value'), 'pm25Value':prn_data.get('pm25Value')})

    with open('동구_신암동_미세먼지.json', 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(json_dust_info, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

json_dust_info = []
make_dust_Json()

