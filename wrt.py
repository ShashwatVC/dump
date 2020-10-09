from lxml import etree as et
def add():
    a = et.Element("a")
    b = et.Element("b")
    a.text = input("LOCK :")
    b.text = input("KEY :")
    root.insert(a)
    root.append(b)
root = et.Element("root")
add()
tree = et.ElementTree(root)
tree.write("sample.xml")
