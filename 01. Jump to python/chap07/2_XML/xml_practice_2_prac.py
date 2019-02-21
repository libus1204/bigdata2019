import xml.etree.ElementTree as etree

data = etree.XML(input)
person = etree.SubElement(data, 'person')
name = etree.SubElement(person, 'Name')
name.text = 'def'
print(etree.tostring(data))