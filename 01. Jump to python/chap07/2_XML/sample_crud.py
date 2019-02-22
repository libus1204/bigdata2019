from xml.etree.ElementTree import parse, ElementTree
tree = parse("sample.xml")
root = tree.getroot()
tags_a = root.find("a")
tags_b = root.find('b')
print(tags_a.attrib.get('name'))
print(tags_b.find('c').text)
print(tags_b.find('c').get('attrib'))
print(tags_a.get("age"))
tags_a.attrib.get('name')
tags_a.attrib.set("name", 'aaa')

#
# print(root.findtext("a"))
# print(a_tags.text)
# a_tags.text = 'eeee'
# print(a_tags.text)
#
ElementTree(root).write("sample.xml")
