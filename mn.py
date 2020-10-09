import csv

def add():
    fn = "cred.csv"
    header = ("NAME","USNM","PWD")
    nm=input("NAME :")
    un=input("USNM :")
    pd=input("PWD :")
    
    data = [
        (nm,un,pd),
    ]

    with open(fn,"w",newline="") as cf:
        creden = csv.writer(cf)
        creden.writerow(header)
        for x in data:
            creden.writerow(x)

add()

