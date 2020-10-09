from lxml import etree

with open("cred.xml",'rb') as f:
    f_c = f.read()
    tree = etree.fromstring(f_c)
    x = input("App :")
    #customer_ids = tree.xpath('//customer/@id')
    #un = tree.xpath('//site[usnm/text()="{}"]/pwd/text()'.format(x))
    #un = tree.xpath('//site/@id={}/pwd/text()'.format(x))
    #print(un)
    un = tree.xpath('//site[name/text()="{}"]/usnm/text()'.format(x))
    for usn in un:
        print("USERNAME = {}".format(usn))
    uno = tree.xpath('//site[name/text()="{}"]/pwd/text()'.format(x))
    for pw in uno:
        print("PASSWORD = {}".format(pw))