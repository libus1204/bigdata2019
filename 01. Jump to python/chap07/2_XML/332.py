from xml.etree.ElementTree import parse

tree = parse("note.xml")
note = tree.getroot()

print(note.get("date"))
print(note.get("foo"))  # 해당 속성 없으면 None 출력
print(note.get("foo", "default"))  # 해당 속성 없으면 뒷 인자를 출력
print(note.keys())  # 속성이 어떤게 있나 출력
print(note.items())  # 속성과 값이 튜플형태로 출력

from_tag = note.find("from")
print(from_tag.text)
from_tags = note.findall("from")
print(from_tags)
from_text = note.findtext("from")
print(from_text) 