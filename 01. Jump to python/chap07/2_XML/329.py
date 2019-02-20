from xml.etree.ElementTree import Element, dump, SubElement

note = Element('note')

to = Element('to')
to.text = "Tove"
note.append(to)

SubElement(note, "from").text = "Jani"  # SubElement 를 활용하여 자식 노드 추가
dump(note)

dummy = Element('dummy')
note.insert(1, dummy)
dump(note)

note.remove(dummy)  # 부모 노드에서 자식 노드를 인자로 넘겨줘야 한다.
dump(note)
