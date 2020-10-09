import xml.etree.ElementTree as ET
tree = ET.parse('cred.xml')
root = tree.getroot()
f = input("site :")
for x in root.iter('site'):
    print(x.attrib)