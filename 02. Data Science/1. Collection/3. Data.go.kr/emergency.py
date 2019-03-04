import urllib.request
from xml.etree.ElementTree import parse
# class GetData:
#     access_key = "QEbF%2Bnfi5HCWciz2PTe%2FWlO%2F1by9CxB8jfRWiyq0IZm%2BrsVxcwMDX%2FkB%2Fb7alBc21fi9EwXCounWbKTu98MDdw%3D%3D"
#     end_point = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire"
#     parameters = "?&serviceKey=" + access_key
#     parameters += "&Q0=%EB%8C%80%EA%B5%AC%EA%B4%91%EC%97%AD%EC%8B%9C"
#     parameters += "&Q1=%EB%8F%99%EA%B5%AC"
#     parameters += "&numOfRows=200"
#
#     url = end_point + parameters
#     def main(self):
#         data = urllib.request.urlopen(self.url).read()
#         f = open('동구_약국.xml', 'wb')
#         f.write(data)
#         f.close()
#
# getData = GetData()
# getData.main()

tree = parse('동구_약국.xml')
root = tree.getroot()
pharmacy_name=[]
pharmacy_phone=[]
pharmacy_addr=[]
for a in root.getiterator("body") :
    for b in a.getiterator("items") :
        pharmacy_tags = b.findall("item")
for i in range(len(pharmacy_tags)) :
    if '신암' in pharmacy_tags[i].findtext("dutyAddr"):
        pharmacy_name.append(pharmacy_tags[i].findtext("dutyName"))
        pharmacy_addr.append(pharmacy_tags[i].findtext("dutyAddr"))
        pharmacy_phone.append(pharmacy_tags[i].findtext("dutyTel1"))

print(pharmacy_name)
print(pharmacy_addr)
print(pharmacy_phone)


