from bs4 import BeautifulSoup
import urllib.request, re
html = urllib.request.urlopen('https://news.naver.com')
soup = BeautifulSoup(html, 'html.parser')
tags = str(soup)
news_politic = []
news_economy = []
news_social = []
news_life = []
news_world = []
news_science = []
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
news_science = []
news_politic_url = []
news_economy_url = []
news_social_url = []
news_life_url = []
news_world_url = []
news_science_url = []
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