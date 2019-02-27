# pip install bs4
from bs4 import BeautifulSoup

html = '''
<html>
Naver 실시간 영화 순위
<td class="title">
<div class="tit3">
<a href="/movie/bi/mi/basic.nhn?code=158191" title="1위 영화">극한직업
</a>
</div>
</td>
</html>
'''
soup = BeautifulSoup(html, 'html.parser')
print(soup)
tag = soup.td
print("\nsoup.td")
print(tag)

tag = soup.div
print("\nsoup.div")
print(tag)

tag = soup.a
print("\nsoup.a")
print(tag)

print("\ntag.name")
print(tag.name)

print("\ntag.attrs")
print(tag.attrs)

print("\ntag.text")
print(tag.text)
print("\ntag.string")
print(tag.string)