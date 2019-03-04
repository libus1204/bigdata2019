from  bs4 import BeautifulSoup
import urllib.request
import re

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

# for count4 in range(len(game_title)):
#     print(game_title[count4], end=" ")
#     print(game_discount[count4][0],end=" ")
#     print(game_price[count4])

p_game_site = re.compile(r'(https://store[.]steampowered[.]com/app/.*_topsellers_.*_.")')
for count4 in range(len(p_game_site.findall(tags))):
    print(p_game_site.findall(tags)[count4])
    # print(len(p_game_site.findall(tags)))
