from lxml import etree
 
with open("sample-customer-xml.xml",'rb') as f:
  file_content = f.read()
  tree = etree.fromstring(file_content)
  # get customer names for customers in LA
  customers_in_la = tree.xpath('//customer[state/text()="LA"]/name/text()')
  for name in customers_in_la:
    print(name)