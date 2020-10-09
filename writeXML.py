import xml.etree.ElementTree as op

def add(x):
    root = op.Element("cred")
    c1 = op.Element("site")
    root.append(c1)
    nm = op.SubElement(c1,"NAME")
    nm.text = input("Name :")

    un = op.SubElement(c1,"USNM")
    un.text = input("USERNAME :")

    pd = op.SubElement(c1,"PWD")
    pd.text = input("PASSWORD :")

    tree = op.ElementTree(root)
    with open(x,"wb") as files:
        tree.write(files)

if __name__=="__main__":
    add("y.xml")