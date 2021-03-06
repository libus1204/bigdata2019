from xml.etree.ElementTree import Element, dump, SubElement, ElementTree

note = Element("note")
note.attrib["date"] = "20120104"

to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"

dump(note)

ElementTree(note).write("note.xml")

SubElement(note, "from").text = "Min"
ElementTree(note).write("note.xml")