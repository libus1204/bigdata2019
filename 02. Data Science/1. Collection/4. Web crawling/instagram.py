import selenium.webdriver as webdriver

print("해쉬태그 검색어를 입력해주세요 : ", end="")
tag = input("#")
url = 'https://www.instagram.com/explore/tags/' + tag

driver = webdriver.Chrome('C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe')

driver.implicitly_wait(5)
driver.get(url)
totalCount = driver.find_element_by_class_name('g47SY').text
print("#%s (으)로 검색한 총 게시글 수는 %s 개 입니다." % (tag, totalCount))

# 열어둔 webdriver를 종료한다
# (종료하지 않고 반복 실행하면 메모리 누수의 원인이 된다)
# driver.quit()