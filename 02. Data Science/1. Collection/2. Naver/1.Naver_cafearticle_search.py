# [참고사항]
# - API 호출수 25,000회 / 일 로 제한
# - 한번 호출에 최대 100개 검색
# - 한번 실행에 최대 1000개 까지 글 검색
# =================================== 카페 검색 ===================================
# 카페 이름 // 글 제목 // 링크 // 요약설명 수집
# 100 * 5 = 500 개 뉴스 수집
import urllib.request
import datetime
import json

app_id="Hg0dhLPJ0jH4hWnGDKk6" # 본인 ID 입력
app_pw="uv8hn6MlfZ" # 본인 Password 입력

def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", app_id)
    req.add_header("X-Naver-Client-Secret", app_pw)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url:%s => Request Success" % (datetime.datetime.now(), url))
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getNaverSearchResult(sNode, search_text, page_start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % sNode
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text), page_start, display)
    url = base+node+parameters
    retData = get_request_url(url)

    if (retData == None):
        return None
    else:
        return json.loads(retData)

def getPostData(post, jsonResult):
    # Data Sampling
    cafename = post['cafename']
    title = post['title']
    link = post['link']
    description = post['description']
    jsonResult.append({'cafename':cafename, 'title':title, 'link':link, 'description':description})
    return

def main():
    jsonResult = []

    sNode = 'cafearticle'
    print("============ 카페 작성 글 빅데이터 수집기 =============")
    search_text = input("검색어를 입력하세요 : ")
    print("\n외부 빅데이터를 수집합니다.")
    display_count = 100

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

    index = 1

    while((jsonSearch!=None) and (jsonSearch['display']!=0) and index<6):
        for post in jsonSearch['items']:
            getPostData(post, jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
        index = index+1

    with open('%s_naver_%s.json' %(search_text, sNode), 'w', encoding='utf8') as outfile:
        retJson = json.dumps(jsonResult, indent=4,sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print("%s_naver_%s.json SAVED" % (search_text, sNode))

if __name__ == '__main__':
    main()